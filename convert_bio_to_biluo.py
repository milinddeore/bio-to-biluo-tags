# -*- coding:utf8 -*-
# !/usr/bin/env python
# Copyright (C) nonymus - All Rights Reserved
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential
# Written by Milind Deore <milind.deore@nonym.us>, June 2023

import spacy
from spacy.training import offsets_to_biluo_tags
nlp = spacy.load("en_core_web_sm")

# Example BIO Annotation
ents = {"classes":["EMAIL","FULL_NAME","FIRST_NAME","GIVEN_NAME","SURNAME"],"annotations":[["This is my full name Milind Madhukar Deore, where Milind is my first name, Madhukar is my given name and Deore is my surname.",{"entities":[[21,42,"FULL_NAME"],[50,56,"FIRST_NAME"],[75,83,"GIVEN_NAME"],[105,110,"SURNAME"]]}],["Working with nonymus and earning $1000",{"entities":[[13,22,"SALARY"]]}],["Lives in Bangalore, India.",{"entities":[[9,18,"LOC"]]}]]}


ents = ents.get('annotations')

with open("biluo_ner.txt","w") as f:
    for sent,tags in ents:
        doc = nlp(sent)
        biluo = offsets_to_biluo_tags(doc,tags['entities'])
        for word,tag in zip(doc, biluo):
            f.write(f"{word} {tag}\n")
        f.write("\n")





