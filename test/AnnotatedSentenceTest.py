import unittest

from AnnotatedSentence.AnnotatedSentence import AnnotatedSentence


class AnnotatedSentenceTest(unittest.TestCase):

    sentence0: AnnotatedSentence
    sentence1: AnnotatedSentence
    sentence2: AnnotatedSentence
    sentence3: AnnotatedSentence
    sentence4: AnnotatedSentence
    sentence5: AnnotatedSentence
    sentence6: AnnotatedSentence
    sentence7: AnnotatedSentence
    sentence8: AnnotatedSentence
    sentence9: AnnotatedSentence

    def setUp(self) -> None:
        self.sentence0 = AnnotatedSentence(open("../sentences/0000.dev", "r", encoding='utf8'), "../sentences/0000.dev")
        self.sentence1 = AnnotatedSentence(open("../sentences/0001.dev", "r", encoding='utf8'), "../sentences/0001.dev")
        self.sentence2 = AnnotatedSentence(open("../sentences/0002.dev", "r", encoding='utf8'), "../sentences/0002.dev")
        self.sentence3 = AnnotatedSentence(open("../sentences/0003.dev", "r", encoding='utf8'), "../sentences/0003.dev")
        self.sentence4 = AnnotatedSentence(open("../sentences/0004.dev", "r", encoding='utf8'), "../sentences/0004.dev")
        self.sentence5 = AnnotatedSentence(open("../sentences/0005.dev", "r", encoding='utf8'), "../sentences/0005.dev")
        self.sentence6 = AnnotatedSentence(open("../sentences/0006.dev", "r", encoding='utf8'), "../sentences/0006.dev")
        self.sentence7 = AnnotatedSentence(open("../sentences/0007.dev", "r", encoding='utf8'), "../sentences/0007.dev")
        self.sentence8 = AnnotatedSentence(open("../sentences/0008.dev", "r", encoding='utf8'), "../sentences/0008.dev")
        self.sentence9 = AnnotatedSentence(open("../sentences/0009.dev", "r", encoding='utf8'), "../sentences/0009.dev")

    def test_GetShallowParseGroups(self):
        self.assertEqual(4, len(self.sentence0.getShallowParseGroups()))
        self.assertEqual(5, len(self.sentence1.getShallowParseGroups()))
        self.assertEqual(3, len(self.sentence2.getShallowParseGroups()))
        self.assertEqual(5, len(self.sentence3.getShallowParseGroups()))
        self.assertEqual(5, len(self.sentence4.getShallowParseGroups()))
        self.assertEqual(5, len(self.sentence5.getShallowParseGroups()))
        self.assertEqual(6, len(self.sentence6.getShallowParseGroups()))
        self.assertEqual(5, len(self.sentence7.getShallowParseGroups()))
        self.assertEqual(5, len(self.sentence8.getShallowParseGroups()))
        self.assertEqual(3, len(self.sentence9.getShallowParseGroups()))

    def test_ContainsPredicate(self):
        self.assertTrue(self.sentence0.containsPredicate())
        self.assertTrue(self.sentence1.containsPredicate())
        self.assertFalse(self.sentence2.containsPredicate())
        self.assertTrue(self.sentence3.containsPredicate())
        self.assertTrue(self.sentence4.containsPredicate())
        self.assertFalse(self.sentence5.containsPredicate())
        self.assertFalse(self.sentence6.containsPredicate())
        self.assertTrue(self.sentence7.containsPredicate())
        self.assertTrue(self.sentence8.containsPredicate())
        self.assertTrue(self.sentence9.containsPredicate())

    def test_GetPredicate(self):
        self.assertEqual("bulandırdı", self.sentence0.getPredicate(0))
        self.assertEqual("yapacak", self.sentence1.getPredicate(0))
        self.assertEqual("ediyorlar", self.sentence3.getPredicate(0))
        self.assertEqual("yazmıştı", self.sentence4.getPredicate(0))
        self.assertEqual("olunacaktı", self.sentence7.getPredicate(0))
        self.assertEqual("gerekiyordu", self.sentence8.getPredicate(0))
        self.assertEqual("ediyor", self.sentence9.getPredicate(0))

    def test_ToStems(self):
        self.assertEqual("devasa ölçek yeni kanun kullan karmaşık ve çetrefil dil kavga bulan .", self.sentence0.toStems())
        self.assertEqual("gelir art usul komite gel salı gün kanun tasarı hakkında bir duruşma yap .", self.sentence1.toStems())
        self.assertEqual("reklam ve tanıtım iş yara yara gör üzere .", self.sentence2.toStems())
        self.assertEqual("bu defa , daha da hız hareket et .", self.sentence3.toStems())
        self.assertEqual("shearson lehman hutton ınc. dün öğle sonra kadar yeni tv reklam yaz .", self.sentence4.toStems())
        self.assertEqual("bu kez , firma hazır .", self.sentence5.toStems())
        self.assertEqual("`` diyalog sür kesinlikle temel önem haiz .", self.sentence6.toStems())
        self.assertEqual("cuma gün bu üzerine düşün çok geç kal ol .", self.sentence7.toStems())
        self.assertEqual("bu hakkında önceden düşün gerek . ''", self.sentence8.toStems())
        self.assertEqual("isim göre çeşit göster birkaç kefaret fon reklam yap için devam et .", self.sentence9.toStems())

    def test_ParserEvaluation(self):
        self.assertEqual(1.0, self.sentence0.compareParses(self.sentence0).getUAS())
        self.assertEqual(1.0, self.sentence0.compareParses(self.sentence0).getLAS())
        self.assertEqual(1.0, self.sentence0.compareParses(self.sentence0).getLS())

if __name__ == '__main__':
    unittest.main()
