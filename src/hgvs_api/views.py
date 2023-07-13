from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import TranscriptSerializer, GDNASerializer

from .handlers import HGVSWrapper

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
        except Exception as e:
            return Response({"error": str(e)}, status=400)
        
        return Response(res, status=200)

class ValidateGDNAView(APIView):
    def post(self, request):
        serializer = GDNASerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        
        # Now that we have a valid serializer, we can access the validated data
        gDNA_variant = serializer.validated_data.get('gDNA_variant')

        hgvs_handler = HGVSWrapper()

        try:
            hgvs_handler.validate_gDNA_variant(gDNA_variant)
        except Exception as e:
            return Response({"error": str(e)}, status=400)

        return Response(gDNA_variant, status=200)