"""
HGVS API serializers
"""

from rest_framework import serializers

class TranscriptSerializer(serializers.Serializer):
    """
    This is just a serializer for receiving the cDNA variant and the hg38 flag.
    Note that validation is done in the handler.
    """
    cDNA_variant = serializers.CharField(
        max_length=100,
        required=True,
    )
    hg38 = serializers.BooleanField(
        default=False,
        required=False,
    )

class GDNASerializer(serializers.Serializer):
    """
    This is just a serializer for receiving the gDNA variant.
    Note that validation is done in the handler.
    """
    gDNA_variant = serializers.CharField(
        max_length=100,
        required=True,
    )
