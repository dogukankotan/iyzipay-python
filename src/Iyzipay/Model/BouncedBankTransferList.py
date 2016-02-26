from src.Iyzipay.HttpClient import HttpClient
from src.Iyzipay.IyzipayResource import IyzipayResource
from src.Iyzipay.JsonBuilder import JsonBuilder
from src.Iyzipay.RequestStringBuilder import RequestStringBuilder


class BouncedBankTransferList(IyzipayResource):
    @classmethod
    def retrieve(cls, request, options):
        json_encoded_request = cls.get_json_object(request)
        pki_string_request = cls.to_pki_request_string(request)
        raw_result = HttpClient.create().post(options['base_url'] + "/reporting/settlement/bounced",
                                              IyzipayResource.get_http_header(pki_string_request, options), json_encoded_request)
        json_result = raw_result.json()
        return json_result

    @classmethod
    def get_json_object(cls, request):
        json_object = JsonBuilder.from_json_object(super(BouncedBankTransferList, cls).get_json_object(request)) \
            .add('date', request['date']) \
            .get_object()
        return JsonBuilder.json_encode(json_object)

    @classmethod
    def to_pki_request_string(cls, request):
        return RequestStringBuilder.create().append_super(super(BouncedBankTransferList, cls).to_pki_request_string(request)) \
            .append('date', request['date']) \
            .get_request_string()