import functions_framework
from twilio.twiml.voice_response import VoiceResponse

def process_request():
    """Respond to incoming phone calls with a brief message."""
    # Start our TwiML response
    resp = VoiceResponse()

    # Read a message aloud to the caller
    resp.say("Yo Boss, how can I help?")

    return str(resp)

@functions_framework.http
def ai_voice_assistant(request):
    # Set CORS headers
    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "POST, OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type",
    }

    # Handle preflight OPTIONS request
    if request.method == "OPTIONS":
        return "", 204, headers
    print(request)
    try:
        result = process_request()
        return result
    except Exception as e:
        print(e)
        return 'Not a valid JSON', 400, headers