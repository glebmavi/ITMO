import xmlplain


def first(text):
  root = xmlplain.xml_to_obj(text, strip_space=True, fold_dict=True)
  with open("1.yml", "w") as outf:
    xmlplain.obj_to_yaml(root, outf)
