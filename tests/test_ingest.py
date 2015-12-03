from unittest import TestCase
from CapitainsFlint.ingest import MyCapytainLocalParser


class TestCapitainParser(TestCase):

    def test_passages(self):
        """ Test that passage retrieving works well
        """
        parsed = MyCapytainLocalParser(
            "xml_resources/1294.002.xml",
            "urn:cts:latinLit:phi1294.phi002:perseus-lat2"
        )
        passages = parsed.getPassages()
        self.assertEqual(
            passages[0],
            ('urn:cts:latinLit:phi1294.phi002:perseus-lat2:1.pr.1', 'Spero me secutum in libellis meis tale temperamen-'),
            "Passages should be formatted well"
        )
        self.assertEqual(
            passages[4],
            ('urn:cts:latinLit:phi1294.phi002:perseus-lat2:1.1.2', 'Toto notus in orbe Martialis '),
            "tei:note should be removed"
        )
        self.assertEqual(
            len(passages),
            11,
            "All passages should be found"
        )