import assemblyai as aai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

aai.settings.api_key = api_key

transcript = aai.Transcriber().transcribe(
    "call.mp3",
    config = aai.TranscriptionConfig(
        redact_pii = True,
        redact_pii_audio=True,
        redact_pii_policies=[
            aai.PIIRedactionPolicy.credit_card_number,
            aai.PIIRedactionPolicy.credit_card_expiration,
            aai.PIIRedactionPolicy.credit_card_cvv,
            aai.PIIRedactionPolicy.email_address,
            aai.PIIRedactionPolicy.phone_number,
            aai.PIIRedactionPolicy.ip_address,
            aai.PIIRedactionPolicy.us_social_security_number,
            aai.PIIRedactionPolicy.location,
            aai.PIIRedactionPolicy.person_name,
            aai.PIIRedactionPolicy.banking_information,
        ]
    )
)

transcript.save_redacted_audio("redacted_audio.mp3")