#!/usr/bin/env python

from lxml import etree
import os, glob, re, datetime, pickle

def lenTest(path,tree):
  return len(tree.xpath(path))

lookupFile = open('/Users/rtillman/Documents/Code/FindingAidsWork_Apparently_Dont_Batch_Ingest/lookup.py', 'r')
lookup = pickle.load(lookupFile)
lookupFile.close()

def cleanerApp(content):
    # Because there are various issues coming through from the unicode stuff, so let's start cleaning this up.
    rdict = {'\xc3\x80':'\u00c0', '\xc3\x81':'\u00c1', '\xc3\x82':'\u00c2', '\xc3\x83':'\u00c3', '\xc3\x84':'\u00c4', '\xc3\x85':'\u00c5', '\xc3\x86':'\u00c6', '\xc3\x87':'\u00c7', '\xc3\x88':'\u00c8', '\xc3\x89':'\u00c9', '\xc3\x8a':'\u00ca', '\xc3\x8b':'\u00cb', '\xc3\x8c':'\u00cc', '\xc3\x8d':'\u00cd', '\xc3\x8e':'\u00ce', '\xc3\x8f':'\u00cf', '\xc3\x90':'\u00d0', '\xc3\x91':'\u00d1', '\xc3\x92':'\u00d2', '\xc3\x93':'\u00d3', '\xc3\x94':'\u00d4', '\xc3\x95':'\u00d5', '\xc3\x96':'\u00d6', '\xc3\x97':'\u00d7', '\xc3\x98':'\u00d8', '\xc3\x99':'\u00d9', '\xc3\x9a':'\u00da', '\xc3\x9b':'\u00db', '\xc3\x9c':'\u00dc', '\xc3\x9d':'\u00dd', '\xc3\x9e':'\u00de', '\xc3\x9f':'\u00df', '\xc3\xa0':'\u00e0', '\xc3\xa1':'\u00e1', '\xc3\xa2':'\u00e2', '\xc3\xa3':'\u00e3', '\xc3\xa4':'\u00e4', '\xc3\xa5':'\u00e5', '\xc3\xa6':'\u00e6', '\xc3\xa7':'\u00e7', '\xc3\xa8':'\u00e8', '\xc3\xa9':'\u00e9', '\xc3\xaa':'\u00ea', '\xc3\xab':'\u00eb', '\xc3\xac':'\u00ec', '\xc3\xad':'\u00ed', '\xc3\xae':'\u00ee', '\xc3\xaf':'\u00ef', '\xc3\xb0':'\u00f0', '\xc3\xb1':'\u00f1', '\xc3\xb2':'\u00f2', '\xc3\xb3':'\u00f3', '\xc3\xb4':'\u00f4', '\xc3\xb5':'\u00f5', '\xc3\xb6':'\u00f6', '\xc3\xb7':'\u00f7', '\xc3\xb8':'\u00f8', '\xc3\xb9':'\u00f9', '\xc3\xba':'\u00fa', '\xc3\xbb':'\u00fb', '\xc3\xbc':'\u00fc', '\xc3\xbd':'\u00fd', '\xc3\xbe':'\u00fe', '\xc3\xbf':'\u00ff', '\xc4\x80':'\u0100', '\xc4\x81':'\u0101', '\xc4\x82':'\u0102', '\xc4\x83':'\u0103', '\xc4\x84':'\u0104', '\xc4\x85':'\u0105', '\xc4\x86':'\u0106', '\xc4\x87':'\u0107', '\xc4\x88':'\u0108', '\xc4\x89':'\u0109', '\xc4\x8a':'\u010a', '\xc4\x8b':'\u010b', '\xc4\x8c':'\u010c', '\xc4\x8d':'\u010d', '\xc4\x8e':'\u010e', '\xc4\x8f':'\u010f', '\xc4\x90':'\u0110', '\xc4\x91':'\u0111', '\xc4\x92':'\u0112', '\xc4\x93':'\u0113', '\xc4\x94':'\u0114', '\xc4\x95':'\u0115', '\xc4\x96':'\u0116', '\xc4\x97':'\u0117', '\xc4\x98':'\u0118', '\xc4\x99':'\u0119', '\xc4\x9a':'\u011a', '\xc4\x9b':'\u011b', '\xc4\x9c':'\u011c', '\xc4\x9d':'\u011d', '\xc4\x9e':'\u011e', '\xc4\x9f':'\u011f', '\xc4\xa0':'\u0120', '\xc4\xa1':'\u0121', '\xc4\xa2':'\u0122', '\xc4\xa3':'\u0123', '\xc4\xa4':'\u0124', '\xc4\xa5':'\u0125', '\xc4\xa6':'\u0126', '\xc4\xa7':'\u0127', '\xc4\xa8':'\u0128', '\xc4\xa9':'\u0129', '\xc4\xaa':'\u012a', '\xc4\xab':'\u012b', '\xc4\xac':'\u012c', '\xc4\xad':'\u012d', '\xc4\xae':'\u012e', '\xc4\xaf':'\u012f', '\xc4\xb0':'\u0130', '\xc4\xb1':'\u0131', '\xc4\xb2':'\u0132', '\xc4\xb3':'\u0133', '\xc4\xb4':'\u0134', '\xc4\xb5':'\u0135', '\xc4\xb6':'\u0136', '\xc4\xb7':'\u0137', '\xc4\xb8':'\u0138', '\xc4\xb9':'\u0139', '\xc4\xba':'\u013a', '\xc4\xbb':'\u013b', '\xc4\xbc':'\u013c', '\xc4\xbd':'\u013d', '\xc4\xbe':'\u013e', '\xc4\xbf':'\u013f', '\xc5\x80':'\u0140', '\xc5\x81':'\u0141', '\xc5\x82':'\u0142', '\xc5\x83':'\u0143', '\xc5\x84':'\u0144', '\xc5\x85':'\u0145', '\xc5\x86':'\u0146', '\xc5\x87':'\u0147', '\xc5\x88':'\u0148', '\xc5\x89':'\u0149', '\xc5\x8a':'\u014a', '\xc5\x8b':'\u014b', '\xc5\x8c':'\u014c', '\xc5\x8d':'\u014d', '\xc5\x8e':'\u014e', '\xc5\x8f':'\u014f', '\xc5\x90':'\u0150', '\xc5\x91':'\u0151', '\xc5\x92':'\u0152', '\xc5\x93':'\u0153', '\xc5\x94':'\u0154', '\xc5\x95':'\u0155', '\xc5\x96':'\u0156', '\xc5\x97':'\u0157', '\xc5\x98':'\u0158', '\xc5\x99':'\u0159', '\xc5\x9a':'\u015a', '\xc5\x9b':'\u015b', '\xc5\x9c':'\u015c', '\xc5\x9d':'\u015d', '\xc5\x9e':'\u015e', '\xc5\x9f':'\u015f', '\xc5\xa0':'\u0160', '\xc5\xa1':'\u0161', '\xc5\xa2':'\u0162', '\xc5\xa3':'\u0163', '\xc5\xa4':'\u0164', '\xc5\xa5':'\u0165', '\xc5\xa6':'\u0166', '\xc5\xa7':'\u0167', '\xc5\xa8':'\u0168', '\xc5\xa9':'\u0169', '\xc5\xaa':'\u016a', '\xc5\xab':'\u016b', '\xc5\xac':'\u016c', '\xc5\xad':'\u016d', '\xc5\xae':'\u016e', '\xc5\xaf':'\u016f', '\xc5\xb0':'\u0170', '\xc5\xb1':'\u0171', '\xc5\xb2':'\u0172', '\xc5\xb3':'\u0173', '\xc5\xb4':'\u0174', '\xc5\xb5':'\u0175', '\xc5\xb6':'\u0176', '\xc5\xb7':'\u0177', '\xc5\xb8':'\u0178', '\xc5\xb9':'\u0179', '\xc5\xba':'\u017a', '\xc5\xbb':'\u017b', '\xc5\xbc':'\u017c', '\xc5\xbd':'\u017d', '\xc5\xbe':'\u017e', '\xc5\xbf':'\u017f', '\xc6\x80':'\u0180', '\xc6\x81':'\u0181', '\xc6\x82':'\u0182', '\xc6\x83':'\u0183', '\xc6\x84':'\u0184', '\xc6\x85':'\u0185', '\xc6\x86':'\u0186', '\xc6\x87':'\u0187', '\xc6\x88':'\u0188', '\xc6\x89':'\u0189', '\xc6\x8a':'\u018a', '\xc6\x8b':'\u018b', '\xc6\x8c':'\u018c', '\xc6\x8d':'\u018d', '\xc6\x8e':'\u018e', '\xc6\x8f':'\u018f', '\xc6\x90':'\u0190', '\xc6\x91':'\u0191', '\xc6\x92':'\u0192', '\xc6\x93':'\u0193', '\xc6\x94':'\u0194', '\xc6\x95':'\u0195', '\xc6\x96':'\u0196', '\xc6\x97':'\u0197', '\xc6\x98':'\u0198', '\xc6\x99':'\u0199', '\xc6\x9a':'\u019a', '\xc6\x9b':'\u019b', '\xc6\x9c':'\u019c', '\xc6\x9d':'\u019d', '\xc6\x9e':'\u019e', '\xc6\x9f':'\u019f', '\xc6\xa0':'\u01a0', '\xc6\xa1':'\u01a1', '\xc6\xa2':'\u01a2', '\xc6\xa3':'\u01a3', '\xc6\xa4':'\u01a4', '\xc6\xa5':'\u01a5', '\xc6\xa6':'\u01a6', '\xc6\xa7':'\u01a7', '\xc6\xa8':'\u01a8', '\xc6\xa9':'\u01a9', '\xc6\xaa':'\u01aa', '\xc6\xab':'\u01ab', '\xc6\xac':'\u01ac', '\xc6\xad':'\u01ad', '\xc6\xae':'\u01ae', '\xc6\xaf':'\u01af', '\xc6\xb0':'\u01b0', '\xc6\xb1':'\u01b1', '\xc6\xb2':'\u01b2', '\xc6\xb3':'\u01b3', '\xc6\xb4':'\u01b4', '\xc6\xb5':'\u01b5', '\xc6\xb6':'\u01b6', '\xc6\xb7':'\u01b7', '\xc6\xb8':'\u01b8', '\xc6\xb9':'\u01b9', '\xc6\xba':'\u01ba', '\xc6\xbb':'\u01bb', '\xc6\xbc':'\u01bc', '\xc6\xbd':'\u01bd', '\xc6\xbe':'\u01be', '\xc6\xbf':'\u01bf', '\xc7\x80':'\u01c0', '\xc7\x81':'\u01c1', '\xc7\x82':'\u01c2', '\xc7\x83':'\u01c3', '\xc7\x84':'\u01c4', '\xc7\x85':'\u01c5', '\xc7\x86':'\u01c6', '\xc7\x87':'\u01c7', '\xc7\x88':'\u01c8', '\xc7\x89':'\u01c9', '\xc7\x8a':'\u01ca', '\xc7\x8b':'\u01cb', '\xc7\x8c':'\u01cc', '\xc7\x8d':'\u01cd', '\xc7\x8e':'\u01ce', '\xc7\x8f':'\u01cf', '\xc7\x90':'\u01d0', '\xc7\x91':'\u01d1', '\xc7\x92':'\u01d2', '\xc7\x93':'\u01d3', '\xc7\x94':'\u01d4', '\xc7\x95':'\u01d5', '\xc7\x96':'\u01d6', '\xc7\x97':'\u01d7', '\xc7\x98':'\u01d8', '\xc7\x99':'\u01d9', '\xc7\x9a':'\u01da', '\xc7\x9b':'\u01db', '\xc7\x9c':'\u01dc', '\xc7\x9d':'\u01dd', '\xc7\x9e':'\u01de', '\xc7\x9f':'\u01df', '\xc7\xa0':'\u01e0', '\xc7\xa1':'\u01e1', '\xc7\xa2':'\u01e2', '\xc7\xa3':'\u01e3', '\xc7\xa4':'\u01e4', '\xc7\xa5':'\u01e5', '\xc7\xa6':'\u01e6', '\xc7\xa7':'\u01e7', '\xc7\xa8':'\u01e8', '\xc7\xa9':'\u01e9', '\xc7\xaa':'\u01ea', '\xc7\xab':'\u01eb', '\xc7\xac':'\u01ec', '\xc7\xad':'\u01ed', '\xc7\xae':'\u01ee', '\xc7\xaf':'\u01ef', '\xc7\xb0':'\u01f0', '\xc7\xb1':'\u01f1', '\xc7\xb2':'\u01f2', '\xc7\xb3':'\u01f3', '\xc7\xb4':'\u01f4', '\xc7\xb5':'\u01f5', '\xc7\xb6':'\u01f6', '\xc7\xb7':'\u01f7', '\xc7\xb8':'\u01f8', '\xc7\xb9':'\u01f9', '\xc7\xba':'\u01fa', '\xc7\xbb':'\u01fb', '\xc7\xbc':'\u01fc', '\xc7\xbd':'\u01fd', '\xc7\xbe':'\u01fe', '\xc7\xbf': '\u01ff'}
    robj = re.compile('|'.join(rdict.keys()))
    content = robj.sub(lambda m: rdict[m.group(0)], content)
    content = re.sub('\s\s+',' ',content)
    content = re.sub(' \.', '.',content)
    content = re.sub(' ,', ',',content)
    content = re.sub(' ;', ';',content)
    content = re.sub(u'(\\n\s|\\n)', '', content)
    return content

def multipleParts(partsPath,tree):
    global creator
    partsList = tree.xpath(partsPath)
    for part in partsList:
        creator = creator + etree.tostring(part, encoding='UTF-8', method='text').strip() + " " # This may need to be edited for your preferred separator between <part> elements.
    creator = creator.strip() + "|"

def multipleCreators(genPath,tree):
    global creator
    num = lenTest(genPath,tree)
    increment = 1
    while increment <= num:
        parts = genPath + "[" + str(increment) + "]" + "/part"
        if lenTest(parts,tree) > 1:
            multipleParts(parts,tree)
        elif lenTest(parts,tree) == 1:
            partsVal = tree.xpath(parts)[0]
            creator = creator + etree.tostring(partsVal, encoding='UTF-8', method='text').strip() + "|"
        increment += 1

def getOrigination(corpXPath, famXPath, nameXPath, persXPath,tree):
    global creator
    if lenTest(corpXPath,tree) > 1:
        multipleCreators(corpXPath,tree)
    elif lenTest(corpXPath,tree) == 1:
        parts = corpXPath + "[1]/part"
        partsVal = tree.xpath(parts)[0]
        creator = creator + etree.tostring(partsVal, encoding='UTF-8', method='text').strip() + "|"
    if lenTest(famXPath,tree) > 1:
        multipleCreators(famXPath,tree)
    elif lenTest(famXPath,tree) == 1:
        parts = famXPath + "[1]/part"
        partsVal = tree.xpath(parts)[0]
        creator = creator + etree.tostring(partsVal, encoding='UTF-8', method='text').strip() + "|"
    if lenTest(nameXPath,tree) > 1:
        multipleCreators(nameXPath,tree)
    elif lenTest(nameXPath,tree) == 1:
        parts = nameXPath + "[1]/part"
        partsVal = tree.xpath(parts)[0]
        creator = creator + etree.tostring(partsVal, encoding='UTF-8', method='text').strip() + "|"
    if lenTest(persXPath,tree) > 1:
        multipleCreators(persXPath,tree)
    elif lenTest(persXPath,tree) == 1:
        parts = persXPath + "[1]/part"
        partsVal = tree.xpath(parts)[0]
        creator = creator + etree.tostring(partsVal, encoding='UTF-8', method='text').strip() + "|"
    creator = cleanerApp(creator)

def getScopeContent(genPath,tree):
    global scopeAndContent
    scopeParagraphPath = genPath + "[1]" + "/p"
    scopeParagraphs = tree.xpath(scopeParagraphPath)
    for para in scopeParagraphs:
        scopeAndContent = scopeAndContent + etree.tostring(para, encoding='UTF-8', method='text').strip() + "\u000a\u000a"
    scopeAndContent = cleanerApp(scopeAndContent)

def stripProcessing(tree, each):
    for instruction in tree.xpath("//processing-instruction('xml-stylesheet')"):
      etree.strip_tags(instruction.getparent() or tree, instruction.tag)
    xml_file = open(each, 'w')
    xml_file.write(etree.tostring(tree, pretty_print=True))
    xml_file.close()

today = datetime.date.today().strftime("%Y_%m_%d")

directory = "/Volumes/curatend-batch/data/EAD_Ingest_Update_" + today # Hardcoded path may have issue if DCNS changes.

titleXPath = "/ead/control/filedesc/titlestmt/titleproper"
scopeXPath = "/ead/archdesc/scopecontent"
corpXPath = "/ead/archdesc/did/origination/corpname"
persXPath = "/ead/archdesc/did/origination/persname"
famXPath = "/ead/archdesc/did/origination/famname"
nameXPath = "/ead/archdesc/did/origination/name"
creator = ""
scopeAndContent = ""

def createCSV(directory, outputFile):
    global creator, scopeAndContent
    os.chdir(directory)
    f = open(outputFile, 'w')
    f.write("type,owner,access,curate_id,files,dc:creator#administrative_unit,dc:title,dc:abstract,dc:creator,dc:source\n") # Non-Notre Dame users will want to remove or replace "type,owner,access". Users may wish to rename "files" (in f.write, not as variable)
    files = glob.glob("*.xml")
    for each in files:
        curate_id = lookup[each]
        tree = etree.parse(each)
        titleString = etree.tostring(tree.xpath(titleXPath)[0], method='text').strip()
        creator = ""
        scopeAndContent = ""
        typeString = "Work-FindingAid" # Non-Notre Dame users will want to remove or replace.
        ownerString = "rtillman" # Non-Notre Dame users will want to remove or replace.
        accessString = "public;edit=rtillman" # Non-Notre Dame users will want to remove or replace.
        departmentString = "University of Notre Dame::Hesburgh Libraries::University Archives"
        identifierString = each.replace(".xml","")
        sourceString = "http://archives.nd.edu/findaids/ead/xml/" + each # Will need to replace with local information or remove dc:source
        titleString = cleanerApp(titleString.replace('"', '\u0022'))
        getOrigination(corpXPath, famXPath, nameXPath, persXPath,tree)
        creator = creator.replace('"', '\u0022')
        getScopeContent(scopeXPath,tree)
        scopeAndContent = scopeAndContent.replace('"', '\u0022')
        creator = '"' + creator + '"'
        titleString = '"' + titleString + '"'
        scopeAndContent = '"' + scopeAndContent + '"'
        line = typeString + "," + ownerString + "," + accessString + "," + curate_id + "," + each + "," + departmentString + "," + titleString + "," + scopeAndContent + "," + creator + "," + sourceString + "\n"
        f.write(line)
        stripProcessing(tree, each)

createCSV(directory,"metadata-1.csv")
