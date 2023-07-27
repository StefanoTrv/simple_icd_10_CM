import unittest
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
        self.assertEqual(cm.get_use_additional_code("A81"),"code to identify:\ndementia with behavioral disturbance (F02.81)\ndementia without behavioral disturbance (F02.80)")
        self.assertEqual(cm.get_use_additional_code("E09"),"code for adverse effect, if applicable, to identify drug (T36-T50 with fifth or sixth character 5)\ncode to identify control using:\ninsulin (Z79.4)\noral antidiabetic drugs (Z79.84)\noral hypoglycemic drugs (Z79.84)")
        self.assertEqual(cm.get_use_additional_code("A17.1"),"")
        self.assertEqual(cm.get_use_additional_code("H60.1"),"")
        self.assertEqual(cm.get_use_additional_code("M84.3"),"external cause code(s) to identify the cause of the stress fracture")
        self.assertEqual(cm.get_use_additional_code("M48.40XS"),"")

    def test_get_code_first(self):
        self.assertEqual(cm.get_code_first("A06"),"")
        self.assertEqual(cm.get_code_first("A81"),"")
        self.assertEqual(cm.get_code_first("E09"),"poisoning due to drug or toxin, if applicable (T36-T65 with fifth or sixth character 1-4 or 6)")
        self.assertEqual(cm.get_code_first("A17.1"),"")
        self.assertEqual(cm.get_code_first("H60.1"),"")
        self.assertEqual(cm.get_code_first("M84.3"),"")
        self.assertEqual(cm.get_code_first("M48.40XS"),"")
        
    def test_get_full_data(self):
        self.assertEqual(cm.get_full_data("E35"),"Name:\nE35\nDescription:\nDisorders of endocrine glands in diseases classified elsewhere\nParent:\nE20-E35\nexcludes1:\nEchinococcus granulosus infection of thyroid gland (B67.3)\nmeningococcal hemorrhagic adrenalitis (A39.1)\nsyphilis of endocrine gland (A52.79)\ntuberculosis of adrenal gland, except calcification (A18.7)\ntuberculosis of endocrine gland NEC (A18.82)\ntuberculosis of thyroid gland (A18.81)\nWaterhouse-Friderichsen syndrome (A39.1)\nuse additional code:\ncode, if applicable, to identify:\nsequelae of tuberculosis of other organs (B90.8)\ncode first:\nunderlying disease, such as:\nlate congenital syphilis of thymus gland [Dubois disease] (A50.5)\nChildren:\nNone")
        self.assertEqual(cm.get_full_data("E40-E46"),"Name:\nE40-E46\nDescription:\nMalnutrition (E40-E46)\nParent:\n4\nexcludes1:\nintestinal malabsorption (K90.-)\nsequelae of protein-calorie malnutrition (E64.0)\nexcludes2:\nnutritional anemias (D50-D53)\nstarvation (T73.0)\nChildren:\nE40, E41, E42, E43, E44, E45, E46")
        self.assertEqual(cm.get_full_data("M48.40XS"),"Name:\nM48.40XS\nDescription:\nFatigue fracture of vertebra, site unspecified, sequela of fracture\nParent:\nM48.40\nChildren:\nNone")
        self.assertEqual(cm.get_full_data("M48.40XS", search_in_ancestors=True),"Name:\nM48.40XS\nDescription:\nFatigue fracture of vertebra, site unspecified, sequela of fracture\nParent:\nM48.40\nseven chr note:\nThe appropriate 7th character is to be added to each code from subcategory M48.4:\nseven chr def:\nA:	initial encounter for fracture\nD:	subsequent encounter for fracture with routine healing\nG:	subsequent encounter for fracture with delayed healing\nS:	sequela of fracture\nChildren:\nNone")

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
        self.assertEqual(cm.get_descendants("G10-G14"),['G10', 'G11', 'G11.0', 'G11.1', 'G11.10', 'G11.11', 'G11.19', 'G11.2', 'G11.3', 'G11.4', 'G11.8', 'G11.9', 'G12', 'G12.0', 'G12.1', 'G12.2', 'G12.20', 'G12.21', 'G12.22', 'G12.23', 'G12.24', 'G12.25', 'G12.29', 'G12.8', 'G12.9', 'G13', 'G13.0', 'G13.1', 'G13.2', 'G13.8', 'G14'])
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
        self.assertEqual(cm.get_all_codes()[27735],'P00')
        self.assertEqual(cm.get_description(cm.get_all_codes()[27735]),'Newborn affected by maternal conditions that may be unrelated to present pregnancy')
        
    def test_get_index(self):
        self.assertEqual(cm.get_index("P00"),27735)
    
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
    
if __name__ == '__main__':
    unittest.main()