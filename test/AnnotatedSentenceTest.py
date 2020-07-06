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
        self.assertEquals(4, len(self.sentence0.getShallowParseGroups()))
        self.assertEquals(5, len(self.sentence1.getShallowParseGroups()))
        self.assertEquals(3, len(self.sentence2.getShallowParseGroups()))
        self.assertEquals(5, len(self.sentence3.getShallowParseGroups()))
        self.assertEquals(5, len(self.sentence4.getShallowParseGroups()))
        self.assertEquals(5, len(self.sentence5.getShallowParseGroups()))
        self.assertEquals(6, len(self.sentence6.getShallowParseGroups()))
        self.assertEquals(5, len(self.sentence7.getShallowParseGroups()))
        self.assertEquals(5, len(self.sentence8.getShallowParseGroups()))
        self.assertEquals(3, len(self.sentence9.getShallowParseGroups()))

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
        self.assertEquals("bulandırdı", self.sentence0.getPredicate(0))
        self.assertEquals("yapacak", self.sentence1.getPredicate(0))
        self.assertEquals("ediyorlar", self.sentence3.getPredicate(0))
        self.assertEquals("yazmıştı", self.sentence4.getPredicate(0))
        self.assertEquals("olunacaktı", self.sentence7.getPredicate(0))
        self.assertEquals("gerekiyordu", self.sentence8.getPredicate(0))
        self.assertEquals("ediyor", self.sentence9.getPredicate(0))

    def test_ToStems(self):
        self.assertEquals("devasa ölçek yeni kanun kullan karmaşık ve çetrefil dil kavga bulan .", self.sentence0.toStems())
        self.assertEquals("gelir art usul komite gel salı gün kanun tasarı hakkında bir duruşma yap .", self.sentence1.toStems())
        self.assertEquals("reklam ve tanıtım iş yara yara gör üzere .", self.sentence2.toStems())
        self.assertEquals("bu defa , daha da hız hareket et .", self.sentence3.toStems())
        self.assertEquals("shearson lehman hutton ınc. dün öğle sonra kadar yeni tv reklam yaz .", self.sentence4.toStems())
        self.assertEquals("bu kez , firma hazır .", self.sentence5.toStems())
        self.assertEquals("`` diyalog sür kesinlikle temel önem haiz .", self.sentence6.toStems())
        self.assertEquals("cuma gün bu üzerine düşün çok geç kal ol .", self.sentence7.toStems())
        self.assertEquals("bu hakkında önceden düşün gerek . ''", self.sentence8.toStems())
        self.assertEquals("isim göre çeşit göster birkaç kefaret fon reklam yap için devam et .", self.sentence9.toStems())


if __name__ == '__main__':
    unittest.main()
