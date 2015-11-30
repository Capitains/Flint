from MyCapytain.resources.texts.local import Text
from elasticsearch import Elasticsearch as ES


class Endpoint(object):
    """ Abstraction for Endpoint

    :param url: URL of the Endpoint
    :type url: str
    :param auth: Authentification information
    :type auth: *
    :param port: Port of the endpoint
    :type port: int

    """
    def __init__(self, url, auth=None, port=None):
        self.url = url
        self.auth = auth
        self.port = port
        self.endpoint = None
        self.register()

    def register(self):
        """ Register the endpoint with init resources
        :return: Endpoint
        """
        raise NotImplementedError()

    def index(self, name, file, passages, index_name="default"):
        """ Index a file according to its name and its xpaths

        :param name: Name of the file to be ingested
        :type name: str
        :param file: Path to the file to be ingested
        :type file: str
        :param passages: List of xpath to ingest
        :type passages: [str]
        :param index_name: Name of the index to use
        :type index_name: str
        :return: Status of success
        :rtype: bool
        """
        raise NotImplementedError()


class ElasticSearch(Endpoint):
    """ ElasticSearch Endpoint implementation

    :param url: URL of the Endpoint
    :type url: str
    :param auth: Authentification information
    :type auth: (str, str)
    :param port: Port of the endpoint
    :type port: int
    """

    def register(self):
        """ Register the endpoint with init resources
        :return: Endpoint
        """
        self.endpoint = ES(self.url, auth=self.auth, port=self.port)
        return self.endpoint


class Parser(object):
    """ Parses an object and return resource with name

    """
    def __init__(self, file, name):
        self.file = file
        self.name = name
        self.text = None
        self.register()

    def register(self):
        """ Ingest the text
        :return: Text object
        """
        raise NotImplementedError()

    def getPassages(self):
        """ Retrieve text passages

        :return: List of duet where first element is the urn and second the text
        :rtype: [(str, str)]
        """

class MyCapytain_Local_Parser(Parser):
    def register(self):
        """ Ingest the text using MyCapytainLocal
        :return: Text object
        :rtype: Text
        """
        with open(self.file) as xml:
            self.text = Text(urn=self.name, resource=xml)

    def getPassages(self):
        passages = []
        for ref in self.text.getValidReff(level=len([citation for citation in self.text.citation])):
            passages.append(
                (
                    "{}:{}".format(self.name, ref),
                    self.text.getPassage(ref.split(".")).text(exclude=["tei:note"])
                )
            )
        return passages