# simple_icd_10_CM
A simple python library for ICD-10_CM codes

This library is a work in progress. The documentation will be updated as I add and/or change features. Expect bugs and major changes until the library is officially released. If you are reading this, it has not been officially released.

## Index
* [Documentation](#documentation)
  * [is_valid_item(code)](#is_valid_itemcode)
  * [is_category_or_subcategory(code)](#is_category_or_subcategorycode)
  * [is_chapter_or_block(code)](#is_chapter_or_blockcode)
  * [is_chapter(code)](#is_chaptercode)
  * [is_block(code)](#is_blockcode)
  * [is_category(code)](#is_categorycode)
  * [is_subcategory(code, include_extended_subcategories=True)](#is_subcategorycode-include_extended_subcategoriestrue)
  * [is_extended_subcategory(code)](#is_extended_subcategorycode)
  * [get_all_codes(keep_dots)](#get_all_codeswith_dotstrue)
  * [get_index(code)](#get_indexcode)

## Documentation
Here I list all the functions provided by this library and describe how to use them. If you are interested in a more interactive introduction to simple_icd_10_cm, please take a look at the [Jupyter Notebook "Showcase notebook.ipynb"](https://github.com/StefanoTrv/simple_icd_10_CM/blob/d736170a378374935277723604e5dd3b82ebae48/Showcase%20notebook.ipynb); there you can also find more examples.

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
This function takes a string as input and returns True if the string is a valid subcategory in ICD-10-CM obtained by adding the 7th character to another code (see [Instructional Notations](https://github.com/StefanoTrv/simple_icd_10_CM/blob/8d15f9bd155567049998f4189fd7e1fc427d143f/Instructional%20Notations.md) for more information), False otherwise.
```python
cm.is_extended_subcategory("S12.000G")
#True
cm.is_extended_subcategory("S12.000")
#False
```

### get_all_codes(with_dots=True)
This function returns the list of all items in the ICD-10-CM classification. If the optional boolean argument `with_dots` is set to False, the subcategories in the list will not have a dot in them, otherwise the subcategories will have a dot in them.
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
