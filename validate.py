from linkml_runtime.loaders import yaml_loader
from linkml_runtime.utils.yamlutils import as_yaml
from linkml_runtime.linkml_model.meta import ClassDefinition
from linkml.generators.pythongen import PythonGenerator
import yaml
from owlready2 import Ontology

"""
Please let this script rn twice, because the first time it will create the file personinfo_tut_7.py, which is needed for the second run.
You will therefore need to delete the commenting marks in the second run.

In this script it is also normal that you will get an error m-runtimessage saying:
    ERROR:root:slot_usage for undefined slot: related_to
    ERROR:root:slot_usage for undefined slot: relationship_type
    ERROR:root:slot_usage for undefined slot: related_to
    ERROR:root:slot_usage for undefined slot: relationship_type
I an in contact with the developers and hope that they can fix this. It should not affect the code however.
"""

#####################################################################################################################
# gen-python personinfo_tut_7.yaml > personinfo_tut_7.py
with open("D://thesis relevant WD//newtemplate3.yaml") as file:
    data = yaml.safe_load(file)

# 'gen_ser' = PythonGenerator(data).serialize()
#
# with open("D://thesis relevant WD//nt3.py", 'w') as outfile:containThe
#     outfile.write(gen_ser)
#####################################################################################################################

from newtemplate3 import Container


#####################################################################################################################
#validating the yaml data file against the class out of the python file
#test_class = yaml.load(data, Loader=yaml.FullLoader)
with open("D://thesis relevant WD//validate set.yaml") as file2:
    data2 = yaml.safe_load(file2)

model = yaml_loader.load(data2, target_class=Container)
####################################################################################################################


###################################################################################

########################################################################################
from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef, RDFS, OWL

# Load the existing OWL ontology into a graph
g = Graph()
g.parse("D://thesis relevant WD//updated_reaction ontology.owl")

# Define the namespace for the ontology
my_namespace = Namespace("http://www.semanticweb.org/gary5/ontologies/2023/5/untitled-ontology-40#")

# Access the elements inside model.reactions directly without wrapping in a list
my_list = model.reactions


# Variables
my_list = model.reactions
products_list = [s.split("#")[-1] for s in g.subjects(RDFS.subClassOf, my_namespace.products)]
main_class = my_namespace['Experiment']       # Create the main test class - Name: Experiment_test
g.add((main_class, RDF.type, RDFS.Class))

for item in my_list:
    # Create a subclass, Name: Experiment_number
    sub_class = my_namespace[item.Experiment_number]
    g.add((sub_class, RDF.type, RDFS.Class))
    g.add((sub_class, RDFS.subClassOf, main_class))

    # Add comments
    if item.Time_on_stream is not None:
        g.add((sub_class, RDF.type, RDFS.Resource))
        g.add((sub_class, RDFS.comment, Literal(str('Time_on_stream: ') + str(item.Time_on_stream))))
    if item.x_CO is not None:
        g.add((sub_class, RDF.type, RDFS.Resource))
        g.add((sub_class, RDFS.comment, Literal(str('x_CO: ') + str(item.x_CO))))
    if item.x_H2 is not None:
        g.add((sub_class, RDF.type, RDFS.Resource))
        g.add((sub_class, RDFS.comment, Literal(str('x_H1: ') + str(item.x_H2))))
    if item.Temperature is not None:
        g.add((sub_class, RDF.type, RDFS.Resource))
        g.add((sub_class, RDFS.comment, Literal(str('Temperature: ') + str(item.Temperature))))
    if item.Volume_Flow is not None:
        g.add((sub_class, RDF.type, RDFS.Resource))
        g.add((sub_class, RDFS.comment, Literal(str('Volume_Flow: ') + str(item.Volume_Flow))))
    if item.Catalyse is not None:
        g.add((sub_class, RDF.type, RDFS.Resource))
        g.add((sub_class, RDFS.comment, Literal(str('Catalyse: ') + str(item.Catalyse))))
    if item.Conversion is not None:
        g.add((sub_class, RDF.type, RDFS.Resource))
        g.add((sub_class, RDFS.comment, Literal(str('Conversion: ') + str(item.Conversion))))

    # subtract the products to the corresponding subclass
    sub_class_products = ''.join(item.Products).replace(' ', '_')

    for p in products_list:
        if p in sub_class_products:     # If the subclass contains a certain product
            # Create a blank node for the restriction
            bnode = BNode()
            # Add property constraint
            g.add((sub_class, RDFS.subClassOf, bnode))
            g.add((bnode, RDF.type, OWL.Restriction))
            g.add((bnode, OWL.onProperty, my_namespace.hasProduct))
            if p == 'None':
                g.add((bnode, OWL.allValuesFrom, my_namespace[p]))
            else:
                g.add((bnode, OWL.someValuesFrom, my_namespace[p]))




# Save the updated ontology to a file
g.serialize(destination='full reaction ontology.owl', format='xml')
