import unittest, warnings
import simple_icd_10_cm as cm

class TestSimpleICD10CM(unittest.TestCase):

    def test_is_valid_item(self):
        self.assertFalse(cm.is_valid_item("dinosaur"))
        self.assertTrue(cm.is_valid_item("12"))
        self.assertTrue(cm.is_valid_item("G10-G14"))
        self.assertTrue(cm.is_valid_item("C00"))
        self.assertTrue(cm.is_valid_item("H60.1"))
        self.assertTrue(cm.is_valid_item("M48.40XS"))

    def test_is_category_or_subcategory(self):
        self.assertFalse(cm.is_category_or_subcategory("dinosaur"))
        self.assertFalse(cm.is_category_or_subcategory("12"))
        self.assertFalse(cm.is_category_or_subcategory("G10-G14"))
        self.assertTrue(cm.is_category_or_subcategory("C00"))
        self.assertTrue(cm.is_category_or_subcategory("H60.1"))
        self.assertTrue(cm.is_category_or_subcategory("M48.40XS"))

    def test_is_chapter_or_block(self):
        self.assertFalse(cm.is_chapter_or_block("dinosaur"))
        self.assertTrue(cm.is_chapter_or_block("12"))
        self.assertTrue(cm.is_chapter_or_block("G10-G14"))
        self.assertFalse(cm.is_chapter_or_block("C00"))
        self.assertFalse(cm.is_chapter_or_block("H60.1"))
        self.assertFalse(cm.is_chapter_or_block("M48.40XS"))

    def test_is_chapter(self):
        self.assertFalse(cm.is_chapter("dinosaur"))
        self.assertTrue(cm.is_chapter("12"))
        self.assertFalse(cm.is_chapter("G10-G14"))
        self.assertFalse(cm.is_chapter("C00"))
        self.assertFalse(cm.is_chapter("H60.1"))
        self.assertFalse(cm.is_chapter("M48.40XS"))

    def test_is_block(self):
        self.assertFalse(cm.is_block("dinosaur"))
        self.assertFalse(cm.is_block("12"))
        self.assertTrue(cm.is_block("G10-G14"))
        self.assertFalse(cm.is_block("C00"))
        self.assertFalse(cm.is_block("H60.1"))
        self.assertFalse(cm.is_block("M48.40XS"))

    def test_is_category(self):
        self.assertFalse(cm.is_category("dinosaur"))
        self.assertFalse(cm.is_category("12"))
        self.assertFalse(cm.is_category("G10-G14"))
        self.assertTrue(cm.is_category("C00"))
        self.assertFalse(cm.is_category("H60.1"))
        self.assertFalse(cm.is_category("M48.40XS"))

    def test_is_subcategory(self):
        self.assertFalse(cm.is_subcategory("dinosaur"))
        self.assertFalse(cm.is_subcategory("12"))
        self.assertFalse(cm.is_subcategory("G10-G14"))
        self.assertFalse(cm.is_subcategory("C00"))
        self.assertTrue(cm.is_subcategory("H60.1"))
        self.assertTrue(cm.is_subcategory("M48.40XS"))
        #setting the optional argument to False
        self.assertFalse(cm.is_subcategory("dinosaur", include_extended_subcategories=False))
        self.assertFalse(cm.is_subcategory("12", include_extended_subcategories=False))
        self.assertFalse(cm.is_subcategory("G10-G14", include_extended_subcategories=False))
        self.assertFalse(cm.is_subcategory("C00", include_extended_subcategories=False))
        self.assertTrue(cm.is_subcategory("H60.1", include_extended_subcategories=False))
        self.assertFalse(cm.is_subcategory("M48.40XS", include_extended_subcategories=False))

    def test_is_extended_subcategory(self):
        self.assertFalse(cm.is_extended_subcategory("dinosaur"))
        self.assertFalse(cm.is_extended_subcategory("12"))
        self.assertFalse(cm.is_extended_subcategory("G10-G14"))
        self.assertFalse(cm.is_extended_subcategory("C00"))
        self.assertFalse(cm.is_extended_subcategory("H60.1"))
        self.assertTrue(cm.is_extended_subcategory("M48.40XS"))
        self.assertFalse(cm.is_extended_subcategory("C44.1192")) #this was not generated automatically!

    def test_get_description(self):
        self.assertEqual(cm.get_description("12"),"Diseases of the skin and subcutaneous tissue (L00-L99)")
        self.assertEqual(cm.get_description("G10-G14"),"Systemic atrophies primarily affecting the central nervous system (G10-G14)")
        self.assertEqual(cm.get_description("C00"),"Malignant neoplasm of lip")
        self.assertEqual(cm.get_description("H60.1"),"Cellulitis of external ear")
        self.assertEqual(cm.get_description("M48.40XS"),"Fatigue fracture of vertebra, site unspecified, sequela of fracture")

    def test_get_excludes1(self):
        self.assertEqual(cm.get_excludes1("A06"),['other protozoal intestinal diseases (A07.-)'])
        self.assertEqual(cm.get_excludes1("A81"),[])
        self.assertEqual(cm.get_excludes1("E09"),['diabetes mellitus due to underlying condition (E08.-)', 'gestational diabetes (O24.4-)', 'neonatal diabetes mellitus (P70.2)', 'postpancreatectomy diabetes mellitus (E13.-)', 'postprocedural diabetes mellitus (E13.-)', 'secondary diabetes mellitus NEC (E13.-)', 'type 1 diabetes mellitus (E10.-)', 'type 2 diabetes mellitus (E11.-)'])
        self.assertEqual(cm.get_excludes1("A17.1"),[])
        self.assertEqual(cm.get_excludes1("H60.1"),[])
        self.assertEqual(cm.get_excludes1("M84.3"),['pathological fracture NOS (M84.4.-)', 'pathological fracture due to osteoporosis (M80.-)', 'traumatic fracture (S12.-, S22.-, S32.-, S42.-, S52.-, S62.-, S72.-, S82.-, S92.-)'])
        self.assertEqual(cm.get_excludes1("M48.40XS"),[])

    def test_get_excludes2(self):
        self.assertEqual(cm.get_excludes2("A06"),['acanthamebiasis (B60.1-)', 'Naegleriasis (B60.2)'])
        self.assertEqual(cm.get_excludes2("A81"),[])
        self.assertEqual(cm.get_excludes2("E09"),[])
        self.assertEqual(cm.get_excludes2("A17.1"),['tuberculoma of brain and spinal cord (A17.81)'])
        self.assertEqual(cm.get_excludes2("H60.1"),[])
        self.assertEqual(cm.get_excludes2("M84.3"),['personal history of (healed) stress (fatigue) fracture (Z87.312)', 'stress fracture of vertebra (M48.4-)'])
        self.assertEqual(cm.get_excludes2("M48.40XS"),[])

    def test_get_includes(self):
        self.assertEqual(cm.get_includes("A06"),['infection due to Entamoeba histolytica'])
        self.assertEqual(cm.get_includes("A81"),['diseases of the central nervous system caused by prions'])
        self.assertEqual(cm.get_includes("E09"),[])
        self.assertEqual(cm.get_includes("A17.1"),[])
        self.assertEqual(cm.get_includes("H60.1"),[])
        self.assertEqual(cm.get_includes("M84.3"),[])
        self.assertEqual(cm.get_includes("M48.40XS"),[])

    def test_get_inclusion_term(self):
        self.assertEqual(cm.get_inclusion_term("A06"),[])
        self.assertEqual(cm.get_inclusion_term("A81"),[])
        self.assertEqual(cm.get_inclusion_term("E09"),[])
        self.assertEqual(cm.get_inclusion_term("A17.1"),['Tuberculoma of meninges (cerebral) (spinal)'])
        self.assertEqual(cm.get_inclusion_term("H60.1"),['Cellulitis of auricle', 'Cellulitis of external auditory canal'])
        self.assertEqual(cm.get_inclusion_term("M84.3"),['Fatigue fracture', 'March fracture', 'Stress fracture NOS', 'Stress reaction'])
        self.assertEqual(cm.get_inclusion_term("M48.40XS"),[])

    def test_get_seven_chr_note(self):
        self.assertEqual(cm.get_seven_chr_note("A06"),"")
        self.assertEqual(cm.get_seven_chr_note("A81"),"")
        self.assertEqual(cm.get_seven_chr_note("E09"),"")
        self.assertEqual(cm.get_seven_chr_note("A17.1"),"")
        self.assertEqual(cm.get_seven_chr_note("H60.1"),"")
        self.assertEqual(cm.get_seven_chr_note("M84.3"),"The appropriate 7th character is to be added to each code from subcategory M84.3:")
        self.assertEqual(cm.get_seven_chr_note("M48.40XS"),"")
        #using search_in_ancestors=True
        self.assertEqual(cm.get_seven_chr_note("M48.40XS", search_in_ancestors=True),"The appropriate 7th character is to be added to each code from subcategory M48.4:")
        

    def test_get_seven_chr_def(self):
        self.assertEqual(cm.get_seven_chr_def("A06"),{})
        self.assertEqual(cm.get_seven_chr_def("A81"),{})
        self.assertEqual(cm.get_seven_chr_def("E09"),{})
        self.assertEqual(cm.get_seven_chr_def("A17.1"),{})
        self.assertEqual(cm.get_seven_chr_def("H60.1"),{})
        self.assertEqual(cm.get_seven_chr_def("M84.3"),{'A': 'initial encounter for fracture', 'D': 'subsequent encounter for fracture with routine healing', 'G': 'subsequent encounter for fracture with delayed healing', 'K': 'subsequent encounter for fracture with nonunion', 'P': 'subsequent encounter for fracture with malunion', 'S': 'sequela'})
        self.assertEqual(cm.get_seven_chr_def("M48.40XS"),{})
        #using search_in_ancestors=True
        self.assertEqual(cm.get_seven_chr_def("M48.40XS", search_in_ancestors=True),{'A': 'initial encounter for fracture', 'D': 'subsequent encounter for fracture with routine healing', 'G': 'subsequent encounter for fracture with delayed healing', 'S': 'sequela of fracture'})

    def test_get_use_additional_code(self):
        self.assertEqual(cm.get_use_additional_code("A06"),"")
        self.assertEqual(cm.get_use_additional_code("A81"),"code, if applicable, to identify:\ndementia with anxiety (F02.84, F02.A4, F02.B4, F02.C4)\ndementia with behavioral disturbance (F02.81-, F02.A1-, F02.B1-, F02.C1-)\ndementia with mood disturbance (F02.83, F02.A3, F02.B3, F02.C3)\ndementia with psychotic disturbance (F02.82, F02.A2, F02.B2, F02.C2)\ndementia without behavioral disturbance (F02.80, F02.A0, F02.B0, F02.C0)\nmild neurocognitive disorder due to known physiological condition (F06.7-)")
        self.assertEqual(cm.get_use_additional_code("E09"),"code for adverse effect, if applicable, to identify drug (T36-T50 with fifth or sixth character 5)\ncode to identify control using:\ninjectable non-insulin antidiabetic drugs (Z79.85)\ninsulin (Z79.4)\noral antidiabetic drugs (Z79.84)\noral hypoglycemic drugs (Z79.84)")
        self.assertEqual(cm.get_use_additional_code("A17.1"),"")
        self.assertEqual(cm.get_use_additional_code("H60.1"),"")
        self.assertEqual(cm.get_use_additional_code("M84.3"),"external cause code(s) to identify the cause of the stress fracture")
        self.assertEqual(cm.get_use_additional_code("M48.40XS"),"")

    def test_get_code_first(self):
        self.assertEqual(cm.get_code_first("A06"),"")
        self.assertEqual(cm.get_code_first("A81"),"")
        self.assertEqual(cm.get_code_first("E09"),"poisoning due to drug or toxin, if applicable (T36-T65 with fifth or sixth character 1-4)")
        self.assertEqual(cm.get_code_first("A17.1"),"")
        self.assertEqual(cm.get_code_first("H60.1"),"")
        self.assertEqual(cm.get_code_first("M84.3"),"")
        self.assertEqual(cm.get_code_first("M48.40XS"),"")
    
    def test_get_code_also(self):
        self.assertEqual(cm.get_code_also("K57.52"),"")
        self.assertEqual(cm.get_code_also("S11"),"any associated:\nspinal cord injury (S14.0, S14.1-)\nwound infection")
        self.assertEqual(cm.get_code_also("Z71.85"),", if applicable, encounter for immunization (Z23)\n, if applicable, immunization not carried out (Z28.-)")
        self.assertEqual(cm.get_code_also("Z77.0"),"")
        self.assertEqual(cm.get_code_also("Z77.0",search_in_ancestors=True),"any follow-up examination (Z08-Z09)")
    
    def test_get_notes(self):
        self.assertEqual(cm.get_notes("K57.52"),"")
        self.assertEqual(cm.get_notes("19"),"Use secondary code(s) from Chapter 20, External causes of morbidity, to indicate cause of injury.  Codes within the T section that include the external cause do not require an additional external cause code\nThe chapter uses the S-section for coding different types of injuries related to single body regions and the T-section to cover injuries to unspecified body regions as well as poisoning and certain other consequences of external causes.")
        self.assertEqual(len(cm.get_notes("V00-V99")),6803)
        self.assertIn("This section is structured in 12 groups.",cm.get_notes("V00-V99"))
        self.assertEqual(cm.get_notes("V91.1"),"select the specified type of watercraft that the victim was on at the time of the collision")
        self.assertEqual(cm.get_notes("Z00.0"),"")
        self.assertEqual(cm.get_notes("Z00.0",search_in_ancestors=True),"Nonspecific abnormal findings disclosed at the time of these examinations are classified to categories R70-R94.")
        
    def test_get_full_data(self):
        self.assertEqual(cm.get_full_data("E35"),"Name:\nE35\nDescription:\nDisorders of endocrine glands in diseases classified elsewhere\nParent:\nE20-E35\nexcludes1:\nEchinococcus granulosus infection of thyroid gland (B67.3)\nmeningococcal hemorrhagic adrenalitis (A39.1)\nsyphilis of endocrine gland (A52.79)\ntuberculosis of adrenal gland, except calcification (A18.7)\ntuberculosis of endocrine gland NEC (A18.82)\ntuberculosis of thyroid gland (A18.81)\nWaterhouse-Friderichsen syndrome (A39.1)\nuse additional code:\ncode, if applicable, to identify:\nsequelae of tuberculosis of other organs (B90.8)\ncode first:\nunderlying disease, such as:\nlate congenital syphilis of thymus gland [Dubois disease] (A50.59)\nChildren:\nNone")
        self.assertEqual(cm.get_full_data("E40-E46"),"Name:\nE40-E46\nDescription:\nMalnutrition (E40-E46)\nParent:\n4\nexcludes1:\nintestinal malabsorption (K90.-)\nsequelae of protein-calorie malnutrition (E64.0)\nexcludes2:\nnutritional anemias (D50-D53)\nstarvation (T73.0)\nChildren:\nE40, E41, E42, E43, E44, E45, E46")
        self.assertEqual(cm.get_full_data("M48.40XS"),"Name:\nM48.40XS\nDescription:\nFatigue fracture of vertebra, site unspecified, sequela of fracture\nParent:\nM48.40\nChildren:\nNone")
        self.assertEqual(cm.get_full_data("M48.40XS", search_in_ancestors=True),"Name:\nM48.40XS\nDescription:\nFatigue fracture of vertebra, site unspecified, sequela of fracture\nParent:\nM48.40\nseven chr note:\nThe appropriate 7th character is to be added to each code from subcategory M48.4:\nseven chr def:\nA:	initial encounter for fracture\nD:	subsequent encounter for fracture with routine healing\nG:	subsequent encounter for fracture with delayed healing\nS:	sequela of fracture\nnotes:\nUse an external cause code following the code for the musculoskeletal condition, if applicable, to identify the cause of the musculoskeletal condition\nChildren:\nNone")
        self.assertEqual(cm.get_full_data("S01"),"Name:\nS01\nDescription:\nOpen wound of head\nParent:\nS00-S09\nexcludes1:\nopen skull fracture (S02.- with 7th character B)\nexcludes2:\ninjury of eye and orbit (S05.-)\ntraumatic amputation of part of head (S08.-)\nseven chr note:\nThe appropriate 7th character is to be added to each code from category S01\nseven chr def:\nA:\tinitial encounter\nD:\tsubsequent encounter\nS:\tsequela\ncode also:\nany associated:\ninjury of cranial nerve (S04.-)\ninjury of muscle and tendon of head (S09.1-)\nintracranial injury (S06.-)\nwound infection\nChildren:\nS01.0, S01.1, S01.2, S01.3, S01.4, S01.5, S01.8, S01.9")
        self.assertEqual(cm.get_full_data("V91.10",search_in_ancestors=True),"Name:\nV91.10\nDescription:\nCrushed between merchant ship and other watercraft or other object due to collision\nParent:\nV91.1\nseven chr note:\nThe appropriate 7th character is to be added to each code from category V91\nseven chr def:\nA:\tinitial encounter\nD:\tsubsequent encounter\nS:\tsequela\nnotes:\nselect the specified type of watercraft that the victim was on at the time of the collision\nChildren:\nV91.10XA, V91.10XD, V91.10XS")

    def test_get_parent(self):
        self.assertEqual(cm.get_parent("12"),"")
        self.assertEqual(cm.get_parent("G10-G14"),"6")
        self.assertEqual(cm.get_parent("C00"),"C00-C14")
        self.assertEqual(cm.get_parent("H60.1"),"H60")
        self.assertEqual(cm.get_parent("M48.40XS"),"M48.40")

    def test_get_children(self):
        self.assertEqual(cm.get_children("12"),['L00-L08', 'L10-L14', 'L20-L30', 'L40-L45', 'L49-L54', 'L55-L59', 'L60-L75', 'L76', 'L80-L99'])
        self.assertEqual(cm.get_children("G10-G14"),['G10', 'G11', 'G12', 'G13', 'G14'])
        self.assertEqual(cm.get_children("C00"),['C00.0', 'C00.1', 'C00.2', 'C00.3', 'C00.4', 'C00.5', 'C00.6', 'C00.8', 'C00.9'])
        self.assertEqual(cm.get_children("H60.1"),['H60.10', 'H60.11', 'H60.12', 'H60.13'])
        self.assertEqual(cm.get_children("M48.40XS"),[])

    def test_get_ancestors(self):
        self.assertEqual(cm.get_ancestors("12"),[])
        self.assertEqual(cm.get_ancestors("G10-G14"),['6'])
        self.assertEqual(cm.get_ancestors("C00"),['C00-C14', '2'])
        self.assertEqual(cm.get_ancestors("H60.1"),['H60', 'H60-H62', '8'])
        self.assertEqual(cm.get_ancestors("M48.40XS"),['M48.40', 'M48.4', 'M48', 'M45-M49', '13'])

    def test_get_descendants(self):
        self.assertEqual(cm.get_descendants("G10-G14"),['G10', 'G11', 'G11.0', 'G11.1', 'G11.10', 'G11.11', 'G11.19', 'G11.2', 'G11.3', 'G11.4', 'G11.5', 'G11.6', 'G11.8', 'G11.9', 'G12', 'G12.0', 'G12.1', 'G12.2', 'G12.20', 'G12.21', 'G12.22', 'G12.23', 'G12.24', 'G12.25', 'G12.29', 'G12.8', 'G12.9', 'G13', 'G13.0', 'G13.1', 'G13.2', 'G13.8', 'G14'])
        self.assertEqual(cm.get_descendants("C00"),['C00.0', 'C00.1', 'C00.2', 'C00.3', 'C00.4', 'C00.5', 'C00.6', 'C00.8', 'C00.9'])
        self.assertEqual(cm.get_descendants("H60.1"),['H60.10', 'H60.11', 'H60.12', 'H60.13'])
        self.assertEqual(cm.get_descendants("M48.40XS"),[])
        
    def test_is_descendant(self):
        self.assertTrue(cm.is_descendant("H60.1","H60-H62"))
        self.assertFalse(cm.is_descendant("H60-H62","H60.1"))
        self.assertFalse(cm.is_descendant("E15-E16","E15-E16"))
        
    def test_is_ancestor(self):
        self.assertFalse(cm.is_ancestor("H60.1","H60-H62"))
        self.assertTrue(cm.is_ancestor("H60-H62","H60.1"))
        self.assertFalse(cm.is_ancestor("E15-E16","E15-E16"))
        
    def test_get_nearest_common_ancestor(self):
        self.assertEqual(cm.get_nearest_common_ancestor("Z52.5","Z52.819"),"Z52")
        
    def test_is_leaf(self):
        self.assertFalse(cm.is_leaf("12"))
        self.assertFalse(cm.is_leaf("G10-G14"))
        self.assertFalse(cm.is_leaf("C00"))
        self.assertFalse(cm.is_leaf("H60.1"))
        self.assertTrue(cm.is_leaf("M48.40XS"))
    
    def test_get_all_codes(self):
        self.assertEqual(cm.get_all_codes()[:15], ['1', 'A00-A09', 'A00', 'A00.0', 'A00.1', 'A00.9', 'A01', 'A01.0', 'A01.00', 'A01.01', 'A01.02', 'A01.03', 'A01.04', 'A01.05', 'A01.09'])
        self.assertEqual(cm.get_all_codes(with_dots=False)[:15], ['1', 'A00-A09', 'A00', 'A000', 'A001', 'A009', 'A01', 'A010', 'A0100', 'A0101', 'A0102', 'A0103', 'A0104', 'A0105', 'A0109'])
        self.assertEqual([code for code in cm.get_all_codes() if not cm.is_chapter_or_block(code)][:15],['A00', 'A00.0', 'A00.1', 'A00.9', 'A01', 'A01.0', 'A01.00', 'A01.01', 'A01.02', 'A01.03', 'A01.04', 'A01.05', 'A01.09', 'A01.1', 'A01.2'])
        self.assertEqual(cm.get_all_codes()[28851],'P00')
        self.assertEqual(cm.get_description(cm.get_all_codes()[28851]),'Newborn affected by maternal conditions that may be unrelated to present pregnancy')
        
    def test_get_index(self):
        self.assertEqual(cm.get_index("P00"),28851)
    
    def test_remove_dot(self):
        self.assertEqual(cm.remove_dot("12"),"12")
        self.assertEqual(cm.remove_dot("G10-G14"),"G10-G14")
        self.assertEqual(cm.remove_dot("H60.1"),"H601")
        self.assertEqual(cm.remove_dot("H601"),"H601")
        self.assertEqual(cm.remove_dot("M48.40XS"),"M4840XS")
        self.assertEqual(cm.remove_dot("M4840XS"),"M4840XS")
    
    def test_add_dot(self):
        self.assertEqual(cm.add_dot("12"),"12")
        self.assertEqual(cm.add_dot("G10-G14"),"G10-G14")
        self.assertEqual(cm.add_dot("H60.1"),"H60.1")
        self.assertEqual(cm.add_dot("H601"),"H60.1")
        self.assertEqual(cm.add_dot("M48.40XS"),"M48.40XS")
        self.assertEqual(cm.add_dot("M4840XS"),"M48.40XS")
    
    def test_new_codes(self):
        self.assertTrue(cm.is_valid_item("U09"))
        self.assertTrue(cm.is_valid_item("A4154"))
    
    def test_loads_all_unique_codes(self):
        self.assertEqual(len(cm.get_all_codes()),97902)
        cm.change_version(all_codes_file_path="all-data/2021-01/code-list-January-2021.txt",classification_data_file_path="all-data/2021-01/icd10cm_tabular_2021.xml")
        self.assertEqual(len(cm.get_all_codes()),95676)
        cm.change_version()


class TestSimpleICD10CMUserData(unittest.TestCase):

    def test_switch_versions(self):
        self.assertTrue(cm.is_valid_item("U09"))
        self.assertEqual(cm.get_full_data("E35"),"Name:\nE35\nDescription:\nDisorders of endocrine glands in diseases classified elsewhere\nParent:\nE20-E35\nexcludes1:\nEchinococcus granulosus infection of thyroid gland (B67.3)\nmeningococcal hemorrhagic adrenalitis (A39.1)\nsyphilis of endocrine gland (A52.79)\ntuberculosis of adrenal gland, except calcification (A18.7)\ntuberculosis of endocrine gland NEC (A18.82)\ntuberculosis of thyroid gland (A18.81)\nWaterhouse-Friderichsen syndrome (A39.1)\nuse additional code:\ncode, if applicable, to identify:\nsequelae of tuberculosis of other organs (B90.8)\ncode first:\nunderlying disease, such as:\nlate congenital syphilis of thymus gland [Dubois disease] (A50.59)\nChildren:\nNone")
        self.assertEqual(cm.get_index("P00"),28851)
        #load January 2021 release
        cm.change_version(all_codes_file_path="all-data/2021-01/code-list-January-2021.txt",classification_data_file_path="all-data/2021-01/icd10cm_tabular_2021.xml")
        self.assertFalse(cm.is_valid_item("U09"))
        self.assertEqual(cm.get_full_data("E35"),"Name:\nE35\nDescription:\nDisorders of endocrine glands in diseases classified elsewhere\nParent:\nE20-E35\nexcludes1:\nEchinococcus granulosus infection of thyroid gland (B67.3)\nmeningococcal hemorrhagic adrenalitis (A39.1)\nsyphilis of endocrine gland (A52.79)\ntuberculosis of adrenal gland, except calcification (A18.7)\ntuberculosis of endocrine gland NEC (A18.82)\ntuberculosis of thyroid gland (A18.81)\nWaterhouse-Friderichsen syndrome (A39.1)\nuse additional code:\ncode, if applicable, to identify:\nsequelae of tuberculosis of other organs (B90.8)\ncode first:\nunderlying disease, such as:\nlate congenital syphilis of thymus gland [Dubois disease] (A50.5)\nChildren:\nNone")
        self.assertEqual(cm.get_index("P00"),27735)
        #restore default version
        cm.change_version()
        self.assertTrue(cm.is_valid_item("U09"))
        self.assertEqual(cm.get_full_data("E35"),"Name:\nE35\nDescription:\nDisorders of endocrine glands in diseases classified elsewhere\nParent:\nE20-E35\nexcludes1:\nEchinococcus granulosus infection of thyroid gland (B67.3)\nmeningococcal hemorrhagic adrenalitis (A39.1)\nsyphilis of endocrine gland (A52.79)\ntuberculosis of adrenal gland, except calcification (A18.7)\ntuberculosis of endocrine gland NEC (A18.82)\ntuberculosis of thyroid gland (A18.81)\nWaterhouse-Friderichsen syndrome (A39.1)\nuse additional code:\ncode, if applicable, to identify:\nsequelae of tuberculosis of other organs (B90.8)\ncode first:\nunderlying disease, such as:\nlate congenital syphilis of thymus gland [Dubois disease] (A50.59)\nChildren:\nNone")
        self.assertEqual(cm.get_index("P00"),28851)
    
    def test_exception_mismatching_arguments(self):
        self.assertRaises(ValueError, lambda: cm.change_version(all_codes_file_path="all-data/2021-01/code-list-January-2021.txt"))
        self.assertRaises(ValueError, lambda: cm.change_version(classification_data_file_path="all-data/2021-01/icd10cm_tabular_2021.xml"))
    
    def test_file_not_found(self):
        self.assertRaises(FileNotFoundError, lambda: cm.change_version(all_codes_file_path="all-data/2021-01/code-list-January-2028.txt",classification_data_file_path="all-data/2021-01/icd10cm_tabular_2021.xml"))
    
    def test_package_works_after_change_exceptions(self):
        try:
            cm.change_version(all_codes_file_path="all-data/2021-01/code-list-January-2021.txt")
        except:
            pass
        self.assertTrue(cm.is_valid_item("U09"))
        self.assertEqual(cm.get_full_data("E35"),"Name:\nE35\nDescription:\nDisorders of endocrine glands in diseases classified elsewhere\nParent:\nE20-E35\nexcludes1:\nEchinococcus granulosus infection of thyroid gland (B67.3)\nmeningococcal hemorrhagic adrenalitis (A39.1)\nsyphilis of endocrine gland (A52.79)\ntuberculosis of adrenal gland, except calcification (A18.7)\ntuberculosis of endocrine gland NEC (A18.82)\ntuberculosis of thyroid gland (A18.81)\nWaterhouse-Friderichsen syndrome (A39.1)\nuse additional code:\ncode, if applicable, to identify:\nsequelae of tuberculosis of other organs (B90.8)\ncode first:\nunderlying disease, such as:\nlate congenital syphilis of thymus gland [Dubois disease] (A50.59)\nChildren:\nNone")
        self.assertEqual(cm.get_index("P00"),28851)
        try:
            cm.change_version(classification_data_file_path="all-data/2021-01/icd10cm_tabular_2021.xml")
        except:
            pass
        self.assertTrue(cm.is_valid_item("U09"))
        self.assertEqual(cm.get_full_data("E35"),"Name:\nE35\nDescription:\nDisorders of endocrine glands in diseases classified elsewhere\nParent:\nE20-E35\nexcludes1:\nEchinococcus granulosus infection of thyroid gland (B67.3)\nmeningococcal hemorrhagic adrenalitis (A39.1)\nsyphilis of endocrine gland (A52.79)\ntuberculosis of adrenal gland, except calcification (A18.7)\ntuberculosis of endocrine gland NEC (A18.82)\ntuberculosis of thyroid gland (A18.81)\nWaterhouse-Friderichsen syndrome (A39.1)\nuse additional code:\ncode, if applicable, to identify:\nsequelae of tuberculosis of other organs (B90.8)\ncode first:\nunderlying disease, such as:\nlate congenital syphilis of thymus gland [Dubois disease] (A50.59)\nChildren:\nNone")
        self.assertEqual(cm.get_index("P00"),28851)
        try:
            cm.change_version(all_codes_file_path="all-data/2021-01/code-list-January-2028.txt",classification_data_file_path="all-data/2021-01/icd10cm_tabular_2021.xml")
        except:
            pass
        self.assertTrue(cm.is_valid_item("U09"))
        self.assertEqual(cm.get_full_data("E35"),"Name:\nE35\nDescription:\nDisorders of endocrine glands in diseases classified elsewhere\nParent:\nE20-E35\nexcludes1:\nEchinococcus granulosus infection of thyroid gland (B67.3)\nmeningococcal hemorrhagic adrenalitis (A39.1)\nsyphilis of endocrine gland (A52.79)\ntuberculosis of adrenal gland, except calcification (A18.7)\ntuberculosis of endocrine gland NEC (A18.82)\ntuberculosis of thyroid gland (A18.81)\nWaterhouse-Friderichsen syndrome (A39.1)\nuse additional code:\ncode, if applicable, to identify:\nsequelae of tuberculosis of other organs (B90.8)\ncode first:\nunderlying disease, such as:\nlate congenital syphilis of thymus gland [Dubois disease] (A50.59)\nChildren:\nNone")
        self.assertEqual(cm.get_index("P00"),28851)

    def test_change_resets_data_structures(self):
        cm.get_all_codes()
        cm.get_index("P00")
        default_length_all_codes = len(cm._all_codes_list)
        default_length_ctn_dict = len(cm._code_to_node)
        number_of_chapters = len(cm._chapter_list)
        #load January 2021 release
        cm.change_version(all_codes_file_path="all-data/2021-01/code-list-January-2021.txt",classification_data_file_path="all-data/2021-01/icd10cm_tabular_2021.xml")
        self.assertEqual(len(cm._chapter_list),number_of_chapters)
        self.assertNotEqual(len(cm._code_to_node),default_length_ctn_dict)
        self.assertEqual(len(cm._all_codes_list),0)
        self.assertEqual(len(cm._all_codes_list_no_dots),0)
        self.assertEqual(len(cm._code_to_index_dictionary),0)
        cm.get_all_codes()
        self.assertGreater(len(cm._all_codes_list),len(cm._code_to_node))
        self.assertNotEqual(len(cm._all_codes_list),default_length_all_codes)
        self.assertNotEqual(len(cm._all_codes_list_no_dots),default_length_all_codes)
        cm.get_index("P00")
        #restore default version
        cm.change_version()
        self.assertEqual(len(cm._chapter_list),number_of_chapters)
        self.assertEqual(len(cm._code_to_node),default_length_ctn_dict)
        self.assertEqual(len(cm._all_codes_list),0)
        self.assertEqual(len(cm._all_codes_list_no_dots),0)
        self.assertEqual(len(cm._code_to_index_dictionary),0)
        cm.get_all_codes()
        self.assertGreater(len(cm._all_codes_list),len(cm._code_to_node))
        self.assertEqual(len(cm._all_codes_list),default_length_all_codes)
        self.assertEqual(len(cm._all_codes_list_no_dots),default_length_all_codes)

class TestSimpleICD10CMWarnings(unittest.TestCase):

    @classmethod
    def tearDownClass(cls): #restores default version after executing all the tests
        super().tearDownClass()
        cm.change_version()

    def everything_else_works(self): #ensures the rest of the data has been loaded correctly
        self.assertTrue(cm.is_valid_item("2"))
        self.assertTrue(cm.is_valid_item("Section_1.2"))
        self.assertTrue(cm.is_valid_item("Led_lightbulb"))
        self.assertTrue(cm.is_valid_item("Brick"))
        self.assertTrue(cm.is_valid_item("Pink_Ninja_upside-down"))
        self.assertEqual(cm.get_parent("Manhole"),"Pet-name")
    
    def test_data_template(self): #ensures the template is working as expected
        cm.change_version(all_codes_file_path="test-data/data-template/list.txt",classification_data_file_path="test-data/data-template/classification.xml")
        self.assertTrue(cm.is_valid_item("2"))
        self.assertTrue(cm.is_valid_item("Section_1.2"))
        self.assertTrue(cm.is_valid_item("Black_Ninja"))
        self.assertTrue(cm.is_valid_item("Black_Ninja_sneakily"))
        self.assertTrue(cm.is_valid_item("Pink_Ninja_standing"))
        self.assertFalse(cm.is_valid_item("Pink_Ninja_sneakily"))
        self.assertIn("warm light",cm.get_includes("Led_lightbulb"))
        self.assertEqual(cm.get_parent("Manhole"),"Pet-name")
    
    def test_warning_extensionless_seven_chr_def_note(self):
        with self.assertWarns(cm._SimpleICD10CMWarning):
            cm.change_version(all_codes_file_path="test-data/seven-chr-def-note-no-text/list.txt",classification_data_file_path="test-data/seven-chr-def-note-no-text/classification.xml")
        self.everything_else_works()

    def test_empty_name_raises_exception(self):
        self.assertRaises(ValueError, lambda: cm.change_version(all_codes_file_path="test-data/name-no-text/list.txt",classification_data_file_path="test-data/name-no-text/classification.xml"))

    def test_empty_desc_warning(self):
        with self.assertWarns(cm._SimpleICD10CMWarning):
            cm.change_version(all_codes_file_path="test-data/desc-no-text/list.txt",classification_data_file_path="test-data/desc-no-text/classification.xml")
        self.everything_else_works()

    def test_empty_includes_warning(self):
        with self.assertWarns(cm._SimpleICD10CMWarning):
            cm.change_version(all_codes_file_path="test-data/includes-no-text/list.txt",classification_data_file_path="test-data/includes-no-text/classification.xml")
        self.everything_else_works()

    def test_empty_seven_chr_note_warning(self):
        with self.assertWarns(cm._SimpleICD10CMWarning):
            cm.change_version(all_codes_file_path="test-data/seven-chr-note-no-text/list.txt",classification_data_file_path="test-data/seven-chr-note-no-text/classification.xml")
        self.everything_else_works()

    def test_code_also_warning(self):
        with self.assertWarns(cm._SimpleICD10CMWarning):
            cm.change_version(all_codes_file_path="test-data/code-also-no-text/list.txt",classification_data_file_path="test-data/code-also-no-text/classification.xml")
        self.everything_else_works()

    def test_warning_suppression_and_enabling(self): # tests that warnings are enabled and disabled correctly and consistently
        with self.assertWarns(cm._SimpleICD10CMWarning):
            cm.change_version(all_codes_file_path="test-data/desc-no-text/list.txt",classification_data_file_path="test-data/desc-no-text/classification.xml")
        self.everything_else_works()
        with warnings.catch_warnings(record=True) as w:
            cm.change_version(all_codes_file_path="test-data/desc-no-text/list.txt",classification_data_file_path="test-data/desc-no-text/classification.xml",suppress_warnings=True)
            self.everything_else_works()
            cm.change_version(all_codes_file_path="test-data/desc-no-text/list.txt",classification_data_file_path="test-data/desc-no-text/classification.xml")
            self.everything_else_works()
            self.assertEqual(len(w), 0)
        with self.assertWarns(cm._SimpleICD10CMWarning):
            cm.change_version(all_codes_file_path="test-data/desc-no-text/list.txt",classification_data_file_path="test-data/desc-no-text/classification.xml",suppress_warnings=False)
        self.everything_else_works()
        with self.assertWarns(cm._SimpleICD10CMWarning):
            cm.change_version(all_codes_file_path="test-data/desc-no-text/list.txt",classification_data_file_path="test-data/desc-no-text/classification.xml")
        self.everything_else_works()
    
if __name__ == '__main__':
    unittest.main()