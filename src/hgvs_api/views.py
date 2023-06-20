from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import TranscriptSerializer

from .handlers import HGVSWrapper

import hgvs.exceptions

class TranscriptView(APIView):
    def post(self, request):
        serializer = TranscriptSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        
        # Now that we have a valid serializer, we can access the validated data
        cDNA_variant = serializer.validated_data.get('cDNA_variant')
        # Check if the user wants the variant in hg38 coordinates
        hg38: bool = serializer.validated_data.get('hg38')

        hgvs_handler = HGVSWrapper()
        try:
            res = hgvs_handler.translate_cDNA_to_genomic(cDNA_variant, hg38=hg38)
        except hgvs.exceptions.HGVSParseError as e:
            return Response(e, status=400)
        
        return Response(res, status=200)
