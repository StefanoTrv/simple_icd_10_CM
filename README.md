# simple_icd_10_CM
A simple python library for ICD-10-CM codes

**This library is a work in progress. The documentation will be updated as I add and/or change features. Expect bugs and major changes until the library is officially released. If you are reading this, it has not been officially released.**

**THE SETUP INSTRUCTIONS FOR PIP AND CONDA WILL NOT WORK UNTIL THE OFFICIAL RELEASE**

## Index
* [Release notes](#release-notes)
* [Introduction](#introduction)
* [Setup](#setup)
* [The format of the codes](#the-format-of-the-codes)
* [About the file "Instructional Notations.md"](#about-the-file-instructional-notationsmd)
* [Blocks containing only one category](#blocks-containing-only-one-category)
* [About the special seventh character](#about-the-special-seventh-character)
* [Documentation](#documentation)
  * [is_valid_item(code)](#is_valid_itemcode)
  * [is_category_or_subcategory(code)](#is_category_or_subcategorycode)
  * [is_chapter_or_block(code)](#is_chapter_or_blockcode)
  * [is_chapter(code)](#is_chaptercode)
  * [is_block(code)](#is_blockcode)
  * [is_category(code)](#is_categorycode)
  * [is_subcategory(code, include_extended_subcategories=True)](#is_subcategorycode-include_extended_subcategoriestrue)
  * [is_extended_subcategory(code)](#is_extended_subcategorycode)
  * [get_description(code, prioritize_blocks=False)](#get_descriptioncode-prioritize_blocksfalse)
  * [get_excludes1(code, prioritize_blocks=False)](#get_excludes1code-prioritize_blocksfalse)
  * [get_excludes2(code, prioritize_blocks=False)](#get_excludes2code-prioritize_blocksfalse)
  * [get_includes(code, prioritize_blocks=False)](#get_includescode-prioritize_blocksfalse)
  * [get_inclusion_term(code, prioritize_blocks=False)](#get_inclusion_termcode-prioritize_blocksfalse)
  * [get_seven_chr_note(code, search_in_ancestors=False, prioritize_blocks=False)](#get_seven_chr_notecode-search_in_ancestorsfalse-prioritize_blocksfalse)
  * [get_seven_chr_def(code, search_in_ancestors=False, prioritize_blocks=False)](#get_seven_chr_defcode-search_in_ancestorsfalse-prioritize_blocksfalse)
  * [get_use_additional_code(code, search_in_ancestors=False, prioritize_blocks=False)](#get_use_additional_codecode-search_in_ancestorsfalse-prioritize_blocksfalse)
  * [get_code_first(code, search_in_ancestors=False, prioritize_blocks=False)](#get_code_firstcode-search_in_ancestorsfalse-prioritize_blocksfalse)
  * [get_parent(code, prioritize_blocks=False)](#get_parentcode-prioritize_blocksfalse)
  * [get_children(code, prioritize_blocks=False)](#get_childrencode-prioritize_blocksfalse)
  * [get_ancestors(code, prioritize_blocks=False)](#get_ancestorscode-prioritize_blocksfalse)
  * [get_descendants(code, prioritize_blocks=False)](#get_descendantscode-prioritize_blocksfalse)
  * [is_ancestor(a,b,prioritize_blocks_a=False,prioritize_blocks_b=False)](#is_ancestorabprioritize_blocks_afalseprioritize_blocks_bfalse)
  * [is_descendant(a,b,prioritize_blocks_a=False,prioritize_blocks_b=False)](#is_descendantabprioritize_blocks_afalseprioritize_blocks_bfalse)
  * [get_nearest_common_ancestor(a,b,prioritize_blocks_a=False,prioritize_blocks_b=False)](#get_nearest_common_ancestorabprioritize_blocks_afalseprioritize_blocks_bfalse)
  * [is_leaf(code, prioritize_blocks=False)](#is_leafcode-prioritize_blocksfalse)
  * [get_all_codes(keep_dots)](#get_all_codeswith_dotstrue)
  * [get_index(code)](#get_indexcode)
  * [remove_dot(code)](#remove_dotcode)
  * [add_dot(code)](#add_dotcode)
* [Conclusion](#conclusion)

## Release notes
None yet

## Introduction
The objective of this library is to provide a simple instrument for dealing with **ICD-10-CM** codes in Python. It provides ways to check whether a code exists, find its ancestors and descendants, see the data associated with it, including its description, and much more.  
If you are looking for a library that deals with ICD-10 codes instead of ICD-10-CM codes, you can check the [simple_icd_10 library](https://github.com/StefanoTrv/simple_icd_10), which is based on the 2019 version of ICD-10.

The data used in this library was taken from the websites of the CDC and of the CMS. This library currently uses the **January 2021 release of ICD-10-CM**.

## Setup
You can install the package with pip, using this command:
```bash
pip install simple-icd-10-cm
```

You can also install the package with conda, using the following command:
```bash
conda install -c stefanotrv simple_icd_10_cm
```

You can also use the "simple_icd_10_cm.py" file, which contains all the source code, in conjunction with the "data" folder, which contains the data used in this library (you can find them in the [GitHub repository](https://github.com/StefanoTrv/simple_icd_10_CM)).

## The format of the codes
The codes of subcategories can be written in two different ways: with a dot (for example "I13.1") and with no dot (for example "I131"). The functions in this library can receive as input codes in both these formats. The codes returned by the functions will always be in the format with the dot.  
You can easily change the format of a code by using the [`remove_dot`](#remove_dotcode) and [`add_dot`](#add_dotcode) functions.

## About the file "Instructional Notations.md"
The file [Instructional Notations.md](https://github.com/StefanoTrv/simple_icd_10_CM/blob/8d15f9bd155567049998f4189fd7e1fc427d143f/Instructional%20Notations.md) contains the introduction present in the file `icd10cm_tabular_2021.xml` (the file that contains the whole ICD-10-CM classification), copied there in a more accessible and readable format. There you can find an explanation about the meaning of most of the additional fields that can accompany a code.

## Blocks containing only one category
Unlike ICD-10, ICD-10-CM includes blocks of categories that contain only one (and its subcategories). These blocks are named after the category that they contain, which means that ICD-10-CM contains blocks and categories that have the same exact code. This is a problem: because of this questionable decision, we can't know for sure if the code "B99", for example, refers to the category "B99" or to the block with the same name. This can be seen in the following example, where "B99" is recognized as both a block and a category:
```python
cm.is_block("B99")
#True
cm.is_category("B99")
#True
```
To solve this ambiguity, I've introduced in most functions the optional argument `prioritize_blocks`. This optional argument has an effect only when the string passed as input could be the name of a category or of its parent block: when this ambiguity is not present, the value of this argument won't have any impact on the computation. When `prioritize_blocks` is False, which is the default value, the ambiguous code will be interpreted as the category, when it's set to True the same code will be interpreted as being the block. The following code shows an example of this in action:
```python
cm.get_children("B99")
#['B99.8', 'B99.9']
cm.get_children("B99",prioritize_blocks=True)
#['B99']
```
If you want to know if a specific code is ambiguous, it's pretty simple: you just have to check if it's at the same time a block and a category, as in the following examples:
```python
cm.is_block("B10") and cm.is_category("B10")
#True
cm.is_block("I12") and cm.is_category("I12")
#False
```

## About the special seventh character
The file `icd10cm_tabular_2021.xml`, which is the XML file that contains the whole ICD-10-CM classification, doesn't have an entry for each code generated by adding the "special" seventh character, but it contains rules that explain how to generate these codes in the "sevenChrDef" field (and sometimes in the "sevenChrNote" field too, just to complicate things a little bit...). You can find more about the structure of these particular codes in [Instructional Notations.md](https://github.com/StefanoTrv/simple_icd_10_CM/blob/8d15f9bd155567049998f4189fd7e1fc427d143f/Instructional%20Notations.md).  
Due to the lack of a complete entry for these codes, I had to decide how they would be handled in this library. So I decided that their only field would be the description, composed of the description of their parent followed by the description of the meaning of the additional character, with a comma between the two: this description appears in official documents about ICD-10-CM (for example in the file `icd10cm-order-Jan-2021.txt`), so it's not my invention but the actual official format. All the other fields are empty, but the optional argument `search_in_ancestors` of certain functions can be used to automatically retrieve the content of certain fields from the ancestors of the code (see the description of the specific functions in the [Documentation](#documentation) for more details).  
If you need to know whether a code has been automatically generated using a rule described in a "sevenChrDef" field, you can use the [`is_extended_subcategory`](#is_extended_subcategorycode) function.

## Documentation
Here I list all the functions provided by this library and describe how to use them. If you are interested in a more interactive introduction to simple_icd_10_cm, please take a look at the Jupyter Notebook ["Showcase notebook.ipynb"](https://github.com/StefanoTrv/simple_icd_10_CM/blob/d736170a378374935277723604e5dd3b82ebae48/Showcase%20notebook.ipynb); there you can also find more examples.

Here I suppose we have imported the library as follows:
```python
import simple_icd_10_cm as cm
```
### is_valid_item(code)
This function takes a string as input and returns True if the string is a valid chapter, block, category or subcategory in ICD-10-CM, False otherwise.
```python
cm.is_valid_item("cat")
#False
cm.is_valid_item("B99")
#True
```
### is_category_or_subcategory(code)
This function takes a string as input and returns True if the string is a valid category or subcategory in ICD-10-CM, False otherwise.
```python
cm.is_category_or_subcategory("A00-B99")
#False
cm.is_category_or_subcategory("B99")
#True
```
### is_chapter_or_block(code)
This function takes a string as input and returns True if the string is a valid chapter or block in ICD-10-CM, False otherwise.
```python
cm.is_chapter_or_block("L80-L99")
#True
cm.is_chapter_or_block("L99")
#False
```
### is_chapter(code)
This function takes a string as input and returns True if the string is a valid chapter in ICD-10-CM, False otherwise.
```python
cm.is_chapter("12")
#True
cm.is_chapter("B99")
#False
```
### is_block(code)
This function takes a string as input and returns True if the string is a valid block in ICD-10-CM, False otherwise.
```python
cm.is_block("L80-L99")
#True
cm.is_block("L99")
#False
```
### is_category(code)
This function takes a string as input and returns True if the string is a valid category in ICD-10-CM, False otherwise.
```python
cm.is_category("B99")
#True
cm.is_category("14")
#False
```
### is_subcategory(code, include_extended_subcategories=True)
This function takes a string as input and returns True if the string is a valid subcategory in ICD-10-CM, False otherwise. By setting the optional argument `include_extended_subcategories` to False, this function will also return False if the string is a valid subcategory obtained by adding the 7th character to another code (see [Instructional Notations](https://github.com/StefanoTrv/simple_icd_10_CM/blob/8d15f9bd155567049998f4189fd7e1fc427d143f/Instructional%20Notations.md) for more information).
```python
cm.is_subcategory("B95.1")
#True
cm.is_subcategory("B99")
#False
cm.is_subcategory("S12.000G")
#True
cm.is_subcategory("S12.000G", include_extended_subcategories=False)
#False
```
### is_extended_subcategory(code)
This function takes a string as input and returns True if the string is a valid subcategory in ICD-10-CM obtained by adding the 7th character to another code (see [Instructional Notations](https://github.com/StefanoTrv/simple_icd_10_CM/blob/8d15f9bd155567049998f4189fd7e1fc427d143f/Instructional%20Notations.md) and [About the special seventh character](#about-the-special-seventh-character) for more information), False otherwise.
```python
cm.is_extended_subcategory("S12.000G")
#True
cm.is_extended_subcategory("S12.000")
#False
```
### get_description(code, prioritize_blocks=False)
This function takes a string as input. If the string is a valid ICD-10-CM code, it returns a **string** containing its description, otherwise it raises a ValueError. For the meaning of the optional argument `prioritize_blocks`, please see [Blocks containing only one category](#blocks-containing-only-one-category).
```python
cm.get_description("12")
#'Diseases of the skin and subcutaneous tissue (L00-L99)'
cm.get_description("I70.501")
#'Unspecified atherosclerosis of nonautologous biological bypass graft(s) of the extremities, right leg'
```
### get_excludes1(code, prioritize_blocks=False)
This function takes a string as input. If the string is a valid ICD-10-CM code, it returns a **list of strings** containing the data of the "excludes1" field of this code, otherwise it raises a ValueError. If this code does not have an "excludes1" field, it returns an empty list. Please see [Instructional Notations](https://github.com/StefanoTrv/simple_icd_10_CM/blob/8d15f9bd155567049998f4189fd7e1fc427d143f/Instructional%20Notations.md) if you have doubts about the meaning of this field. For the meaning of the optional argument `prioritize_blocks`, please see [Blocks containing only one category](#blocks-containing-only-one-category).
```python
cm.get_excludes1("12")
#[]
cm.get_excludes1("I82.40")
#['acute embolism and thrombosis of unspecified deep veins of distal lower extremity (I82.4Z-)',
# 'acute embolism and thrombosis of unspecified deep veins of proximal lower extremity (I82.4Y-)']
```
### get_excludes2(code, prioritize_blocks=False)
This function takes a string as input. If the string is a valid ICD-10-CM code, it returns a **list of strings** containing the data of the "excludes2" field of this code, otherwise it raises a ValueError. If this code does not have an "excludes2" field, it returns an empty list. Please see [Instructional Notations](https://github.com/StefanoTrv/simple_icd_10_CM/blob/8d15f9bd155567049998f4189fd7e1fc427d143f/Instructional%20Notations.md) if you have doubts about the meaning of this field. For the meaning of the optional argument `prioritize_blocks`, please see [Blocks containing only one category](#blocks-containing-only-one-category).
```python
cm.get_excludes2("I82.40")
#[]
cm.get_excludes2("J34.81")
#['gastrointestinal mucositis (ulcerative) (K92.81)',
# 'mucositis (ulcerative) of vagina and vulva (N76.81)',
# 'oral mucositis (ulcerative) (K12.3-)']
```
### get_includes(code, prioritize_blocks=False)
This function takes a string as input. If the string is a valid ICD-10-CM code, it returns a **list of strings** containing the data of the "includes" field of this code, otherwise it raises a ValueError. If this code does not have an "includes" field, it returns an empty list. Please see [Instructional Notations](https://github.com/StefanoTrv/simple_icd_10_CM/blob/8d15f9bd155567049998f4189fd7e1fc427d143f/Instructional%20Notations.md) if you have doubts about the meaning of this field. For the meaning of the optional argument `prioritize_blocks`, please see [Blocks containing only one category](#blocks-containing-only-one-category).
```python
cm.get_includes("I82.40")
#[]
cm.get_includes("J36")
#['abscess of tonsil', 'peritonsillar cellulitis', 'quinsy']
```
### get_inclusion_term(code, prioritize_blocks=False)
This function takes a string as input. If the string is a valid ICD-10-CM code, it returns a **list of strings** containing the data of the "inclusionTerm" field of this code, otherwise it raises a ValueError. If this code does not have an "inclusionTerm" field, it returns an empty list. For the meaning of the optional argument `prioritize_blocks`, please see [Blocks containing only one category](#blocks-containing-only-one-category).
```python
cm.get_inclusion_term("A23")
#[]
cm.get_inclusion_term("J37.0")
#['Catarrhal laryngitis', 'Hypertrophic laryngitis', 'Sicca laryngitis']
```
### get_seven_chr_note(code, search_in_ancestors=False, prioritize_blocks=False)
This function takes a string as input. If the string is a valid ICD-10-CM code, it returns a **string** containing the data of the "sevenChrNote" field of this code, otherwise it raises a ValueError. If this code does not have an "sevenChrNote" field, it returns an empty list. Please see [Instructional Notations](https://github.com/StefanoTrv/simple_icd_10_CM/blob/8d15f9bd155567049998f4189fd7e1fc427d143f/Instructional%20Notations.md) and [About the special seventh character](#about-the-special-seventh-character) if you have doubts about the meaning of this field. When the optional argument `search_in_ancestors` is set to True, if the given code doesn't have a "sevenChrNote" field but one of its ancestor does, the "sevenChrNote" data of the closer ancestor that contains such a field is returned. For the meaning of the optional argument `prioritize_blocks`, please see [Blocks containing only one category](#blocks-containing-only-one-category).
```python
cm.get_seven_chr_note("I82.40")
#''
cm.get_seven_chr_note("M48.4")
#'The appropriate 7th character is to be added to each code from subcategory M48.4:'
cm.get_seven_chr_note("R40.241")
#''
cm.get_seven_chr_note("R40.241",search_in_ancestors=True)
#'The following appropriate 7th character is to be added to subcategory R40.24-:'
```
### get_seven_chr_def(code, search_in_ancestors=False, prioritize_blocks=False)
This function takes a string as input. If the string is a valid ICD-10-CM code, it returns a **dictionary** containing the data of the "sevenChrDef" field of this code, otherwise it raises a ValueError. The dictionary maps the seventh character to a string that contains its meaning. If this code does not have an "sevenChrDef" field, it returns an empty list. Please see [Instructional Notations](https://github.com/StefanoTrv/simple_icd_10_CM/blob/8d15f9bd155567049998f4189fd7e1fc427d143f/Instructional%20Notations.md) and [About the special seventh character](#about-the-special-seventh-character) if you have doubts about the meaning of this field. When the optional argument `search_in_ancestors` is set to True, if the given code doesn't have a "sevenChrDef" field but one of its ancestor does, the "sevenChrDef" data of the closer ancestor that contains such a field is returned. For the meaning of the optional argument `prioritize_blocks`, please see [Blocks containing only one category](#blocks-containing-only-one-category).
```python
cm.get_seven_chr_def("I82.40")
#{}
cm.get_seven_chr_def("M48.4")
#{'A': 'initial encounter for fracture',
# 'D': 'subsequent encounter for fracture with routine healing',
# 'G': 'subsequent encounter for fracture with delayed healing',
# 'S': 'sequela of fracture'}
cm.get_seven_chr_def("R40.241")
#{}
cm.get_seven_chr_def("R40.241",search_in_ancestors=True)
#{'0': 'unspecified time',
# '1': 'in the field [EMT or ambulance]',
# '2': 'at arrival to emergency department',
# '3': 'at hospital admission',
# '4': '24 hours or more after hospital admission'}
```
### get_use_additional_code(code, search_in_ancestors=False, prioritize_blocks=False)
This function takes a string as input. If the string is a valid ICD-10-CM code, it returns a **string** containing the data of the "useAdditionalCode" field of this code, otherwise it raises a ValueError. If this code does not have an "useAdditionalCode" field, it returns an empty list. Please see [Instructional Notations](https://github.com/StefanoTrv/simple_icd_10_CM/blob/8d15f9bd155567049998f4189fd7e1fc427d143f/Instructional%20Notations.md) if you have doubts about the meaning of this field. When the optional argument `search_in_ancestors` is set to True, if the given code doesn't have a "useAdditionalCode" field but one of its ancestor does, the "useAdditionalCode" data of the closer ancestor that contains such a field is returned. For the meaning of the optional argument `prioritize_blocks`, please see [Blocks containing only one category](#blocks-containing-only-one-category).
```python
cm.get_use_additional_code("I82.41")
#''
cm.get_use_additional_code("R50.2")
#'code for adverse effect, if applicable, to identify drug (T36-T50 with fifth or sixth character 5)'
cm.get_use_additional_code("R65.20")
#''
cm.get_use_additional_code("R65.20",search_in_ancestors=True)
#'code to identify specific acute organ dysfunction, such as:
# acute kidney failure (N17.-)
# acute respiratory failure (J96.0-)
# critical illness myopathy (G72.81)
# critical illness polyneuropathy (G62.81)
# disseminated intravascular coagulopathy [DIC] (D65)
# encephalopathy (metabolic) (septic) (G93.41)
# hepatic failure (K72.0-)'
```
### get_code_first(code, search_in_ancestors=False, prioritize_blocks=False)
This function takes a string as input. If the string is a valid ICD-10-CM code, it returns a **string** containing the data of the "codeFirst" field of this code, otherwise it raises a ValueError. If this code does not have an "codeFirst" field, it returns an empty list. Please see [Instructional Notations](https://github.com/StefanoTrv/simple_icd_10_CM/blob/8d15f9bd155567049998f4189fd7e1fc427d143f/Instructional%20Notations.md) if you have doubts about the meaning of this field. When the optional argument `search_in_ancestors` is set to True, if the given code doesn't have a "codeFirst" field but one of its ancestor does, the "codeFirst" data of the closer ancestor that contains such a field is returned. For the meaning of the optional argument `prioritize_blocks`, please see [Blocks containing only one category](#blocks-containing-only-one-category).
```python
cm.get_code_first("I82.41")
#''
cm.get_code_first("R68.13")
#'confirmed diagnosis, if known'
cm.get_code_first("S04.01")
#''
cm.get_code_first("S04.01",search_in_ancestors=True)
#'any associated intracranial injury (S06.-)'
```
### get_full_data(code, search_in_ancestors=False, prioritize_blocks=False)
This function takes a string as input. If the string is a valid ICD-10-CM code, it returns a string containing the all the available data of the code, otherwise it raises a ValueError. The empty fields are omitted from the string, except for the list of children (see second example below). When the optional argument `search_in_ancestors` is set to True, if the given code doesn't have a certain field but one of its ancestor does, the data of the closer ancestor that contains such a field is returned: see the previous functions to know which are the fields that are influenced by this argument and which are not. For the meaning of the optional argument `prioritize_blocks`, please see [Blocks containing only one category](#blocks-containing-only-one-category).
```python
cm.get_full_data("I82.41")
#'Name:
# I82.41
# Description:
# Acute embolism and thrombosis of femoral vein
# Parent:
# I82.4
# inclusion term:
# Acute embolism and thrombosis of common femoral vein
# Acute embolism and thrombosis of deep femoral vein
# Children:
# I82.411, I82.412, I82.413, I82.419'
cm.get_full_data("C8401")
#'Name:
# C84.01
# Description:
# Mycosis fungoides, lymph nodes of head, face, and neck
# Parent:
# C84.0
# Children:
# None'
```
### get_parent(code, prioritize_blocks=False)
This function takes a string as input. If the string is a valid ICD-10-CM code, it returns a string containing its parent, otherwise it raises a ValueError. If the code doesn't have a parent (that is, if it's a chapter), it returns an empty string. For the meaning of the optional argument `prioritize_blocks`, please see [Blocks containing only one category](#blocks-containing-only-one-category).
```python
cm.get_parent("I70.501")
#'I70.50'
cm.get_parent("12")
#''
```
### get_children(code, prioritize_blocks=False)
This function takes a string as input. If the string is a valid ICD-10-CM code, it returns a list of strings containing its children, otherwise it raises a ValueError. If the code doesn't have children, it returns an empty list. For the meaning of the optional argument `prioritize_blocks`, please see [Blocks containing only one category](#blocks-containing-only-one-category).
```python
cm.get_children("12")
#['L00-L08', 'L10-L14', 'L20-L30', 'L40-L45', 'L49-L54', 'L55-L59', 'L60-L75', 'L76', 'L80-L99']
cm.get_children("I70.501")
#[]
```
### get_ancestors(code, prioritize_blocks=False)
This function takes a string as input. If the string is a valid ICD-10-CM code, it returns a list containing all its ancestors in the ICD-10-CM classification, otherwise it raises a ValueError. The results are ordered from its parent to its most distant ancestor. For the meaning of the optional argument `prioritize_blocks`, please see [Blocks containing only one category](#blocks-containing-only-one-category).
```python
cm.get_ancestors("S14.109S")
#['S14.109', 'S14.10', 'S14.1', 'S14', 'S10-S19', '19']
cm.get_ancestors("7")
#[]
```
### get_descendants(code, prioritize_blocks=False)
This function takes a string as input. If the string is a valid ICD-10-CM code, it returns a list containing all its descendants in the ICD-10-CM classification, otherwise it raises a ValueError. The returned codes are ordered as in a pre-order depth-first traversal of the tree containing the ICD-10-CM classification. For the meaning of the optional argument `prioritize_blocks`, please see [Blocks containing only one category](#blocks-containing-only-one-category).
```python
cm.get_descendants("G93")
#['G93.0', 'G93.1', 'G93.2', 'G93.3', 'G93.4', 'G93.40', 'G93.41', 'G93.49', 'G93.5', 'G93.6', 'G93.7', 'G93.8', 'G93.81', 'G93.82', 'G93.89', 'G93.9']
cm.get_descendants("S14.109S")
#[]
```
### is_ancestor(a,b,prioritize_blocks_a=False,prioritize_blocks_b=False)
This function takes two strings as input. If both strings are valid ICD-10-CM codes, it returns True if the first string is an ancestor of the second string. If at least one of the strings is not a valid ICD-10-CM code, it raises a ValueError. The optional arguments `prioritize_blocks_a` and `prioritize_blocks_b` refer, respectively, to the codes in `a` and in `b`; please see [Blocks containing only one category](#blocks-containing-only-one-category) for the meaning of these optional arguments.
```python
cm.is_ancestor("18","R01.0")
#True
cm.is_ancestor("K00-K14","M31")
#False
cm.is_ancestor("B99","B99")
#False
cm.is_ancestor("B99","B99",prioritize_blocks_a=True)
#True
```
### is_descendant(a,b,prioritize_blocks_a=False,prioritize_blocks_b=False)
This function takes two strings as input. If both strings are valid ICD-10-CM codes, it returns True if the first string is a descendant of the second string. If at least one of the strings is not a valid ICD-10-CM code, it raises a ValueError. The optional arguments `prioritize_blocks_a` and `prioritize_blocks_b` refer, respectively, to the codes in `a` and in `b`; please see [Blocks containing only one category](#blocks-containing-only-one-category) for the meaning of these optional arguments.
```python
cm.is_descendant("R01.0","18")
#True
cm.is_descendant("M31","K00-K14")
#False
```
### get_nearest_common_ancestor(a,b,prioritize_blocks_a=False,prioritize_blocks_b=False)
This function takes two strings as input. If both strings are valid ICD-10-CM codes, it returns the nearest common ancestor if it exists, an empty string if it doesn't exist. If at least one of the strings is not a valid ICD-10-CM code, it raises a ValueError. The optional arguments `prioritize_blocks_a` and `prioritize_blocks_b` refer, respectively, to the codes in `a` and in `b`; please see [Blocks containing only one category](#blocks-containing-only-one-category) for the meaning of these optional arguments.
```python
cm.get_nearest_common_ancestor("H28","H25.1")
#'H25-H28'
cm.get_nearest_common_ancestor("K35","E21.0")
#''
```
### is_leaf(code, prioritize_blocks=False)
This function takes a string as input. If the string is a valid ICD-10-CM code, it returns True if it's a leaf in the ICD-10-CM classification (that is, if it has no children), otherwise it returns False. If the string is not a valid ICD-10-CM code it raises a ValueError. For the meaning of the optional argument `prioritize_blocks`, please see [Blocks containing only one category](#blocks-containing-only-one-category).
```python
cm.is_leaf("12")
#False
cm.is_leaf("I70.501")
#True
```
### get_all_codes(with_dots=True)
This function returns the list of all items in the ICD-10-CM classification. If the optional boolean argument `with_dots` is set to False, the subcategories in the list will not have a dot in them, otherwise the subcategories will have a dot in them. The codes that represent both a block and a category (for example "B99") appear only once in this list.
```python
cm.get_all_codes()
#['1', 'A00-A09', 'A00', 'A00.0', 'A00.1', 'A00.9', 'A01', 'A01.0', ...
cm.get_all_codes(False)
#['1', 'A00-A09', 'A00', 'A000', 'A001', 'A009', 'A01', 'A010', ...
```
### get_index(code)
This function takes a string as input. If the string is a valid ICD-10-CM code, it returns its index in the list returned by `get_all_codes`, otherwise it raises a ValueError.
```python
cm.get_index("P00")
#27735
cm.get_all_codes(True)[27735]
#"P00"
```
### remove_dot(code)
This function takes a string as input. If the string is a valid ICD-10-CM code, it returns the same code in the notation without the dot, otherwise it raises a ValueError.
```python
cm.remove_dot("C84.Z0")
#'C84Z0'
cm.remove_dot("C84Z0")
#'C84Z0'
cm.remove_dot("K00-K14")
#'K00-K14'
```
### add_dot(code)
This function takes a string as input. If the string is a valid ICD-10-CM code, it returns the same code in the notation with the dot, otherwise it raises a ValueError.
```python
cm.add_dot("C84Z0")
#'C84.Z0'
cm.add_dot("C84.Z0")
#'C84.Z0'
cm.add_dot("K00-K14")
#'K00-K14'
```

## Conclusion
This should be everything you need to know about the simple_icd_10_CM library. Please contact me if you find any mistake, bug, missing feature or anything else that could be improved or made easier to comprehend, both in this documentation and in the library itself as well as in the [Showcase notebook](https://github.com/StefanoTrv/simple_icd_10_CM/blob/d736170a378374935277723604e5dd3b82ebae48/Showcase%20notebook.ipynb). You can also contact me if you need any help using this library, but I may not be able to help with questions about the ICD-10-CM classification itself. This library currently only support the January 2021 release of ICD-10-CM: let me know if you'd like me to implement the ability to switch between different versions of ICD-10-CM, and also tell me which release or releases you are interested in.

If you find this library useful and are feeling generous, consider making a donation using one of the methods listed at the end of this document.

*Stefano Travasci*

---

Paypal: [![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif)](https://www.paypal.com/donate?hosted_button_id=9HMMFAZE248VN)

Curecoin: BKxCWuWzsqtLzAvAjtpsHpJ7LqFHPubqft

Bitcoin: bc1qjtnvzzgpsxz397l03vhrw8l30vl2p7fepmn5yy

<sub>*let me know if your favorite donation method is not in this list*</sub>
