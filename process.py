from lxml import etree
import os, glob

def lenTest(path,tree):
  return len(tree.xpath(path))

def multipleParts(partsPath,tree):
    global creator
    partsList = tree.xpath(partsPath)
    for part in partsList:
        creator = creator + etree.tostring(part, encoding='unicode_escape', method='text').strip() + "|"

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
            creator = creator + etree.tostring(partsVal, encoding='unicode_escape', method='text').strip() + "|"
        increment += 1

def getOrigination(corpXPath, famXPath, nameXPath, persXPath,tree):
    global creator
    if lenTest(corpXPath,tree) > 1:
        multipleCreators(corpXPath,tree)
    elif lenTest(corpXPath,tree) == 1:
        parts = corpXPath + "[1]/part"
        partsVal = tree.xpath(parts)[0]
        creator = creator + etree.tostring(partsVal, encoding='unicode_escape', method='text').strip() + "|"
    if lenTest(famXPath,tree) > 1:
        multipleCreators(famXPath,tree)
    elif lenTest(famXPath,tree) == 1:
        parts = famXPath + "[1]/part"
        partsVal = tree.xpath(parts)[0]
        creator = creator + etree.tostring(partsVal, encoding='unicode_escape', method='text').strip() + "|"
    if lenTest(nameXPath,tree) > 1:
        multipleCreators(nameXPath,tree)
    elif lenTest(nameXPath,tree) == 1:
        parts = nameXPath + "[1]/part"
        partsVal = tree.xpath(parts)[0]
        creator = creator + etree.tostring(partsVal, encoding='unicode_escape', method='text').strip() + "|"
    if lenTest(persXPath,tree) > 1:
        multipleCreators(persXPath,tree)
    elif lenTest(persXPath,tree) == 1:
        parts = persXPath + "[1]/part"
        partsVal = tree.xpath(parts)[0]
        creator = creator + etree.tostring(partsVal, encoding='unicode_escape', method='text').strip() + "|"

def getScopeContent(genPath,tree):
    global scopeAndContent
    scopeParagraphPath = genPath + "[1]" + "/p"
    scopeParagraphs = tree.xpath(scopeParagraphPath)
    for para in scopeParagraphs:
        scopeAndContent = scopeAndContent + etree.tostring(para, encoding='unicode_escape', method='text').strip() + "\u000a\u000a"

directory = "/Users/rtillman/Documents/Code/FindingAidsWork_Apparently_Dont_Batch_Ingest/samples" # Hardcoded. May need to be replaced.

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
    f.write("type,owner,access,files,dc:title,dc:abstract,dc:creator,dc:identifier\n") # Non-Notre Dame users will want to remove or replace "type,owner,access". Users may wish to rename "files" (in f.write, not as variable)
    files = glob.glob("*.xml")
    for each in files:
        tree = etree.parse(each)
        titleString = etree.tostring(tree.xpath(titleXPath)[0], method='text').strip()
        creator = ""
        scopeAndContent = ""
        typeString = "Work-FindingAid" # Non-Notre Dame users will want to remove or replace.
        ownerString = "rtillman" # Non-Notre Dame users will want to remove or replace.
        accessString = "public;edit=rtillman" # Non-Notre Dame users will want to remove or replace.
        identifierString = each.replace(".xml","")
        titleString = titleString.replace('"', '\u0022')
        getOrigination(corpXPath, famXPath, nameXPath, persXPath,tree)
        creator = creator.replace('"', '\u0022')
        getScopeContent(scopeXPath,tree)
        scopeAndContent = scopeAndContent.replace('"', '\u0022')
        creator = '"' + creator + '"'
        titleString = '"' + titleString + '"'
        scopeAndContent = '"' + scopeAndContent + '"'
        line = typeString + "," + ownerString  + "," + accessString + "," + each + "," + titleString + "," + scopeAndContent + "," + creator + "," + identifierString + "\n"
        f.write(line)

output = raw_input("What do you want to call the file? ")
createCSV(directory,output)
