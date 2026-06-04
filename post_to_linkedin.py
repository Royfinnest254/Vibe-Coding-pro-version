import os
import sys
import requests

# Strict configuration checks
ACCESS_TOKEN = os.getenv("LINKEDIN_ACCESS_TOKEN")
if not ACCESS_TOKEN:
    print("[ERROR] Environment variable LINKEDIN_ACCESS_TOKEN is missing.", file=sys.stderr)
    print("[ERROR] Exiting execution. Please set it before running the script.", file=sys.stderr)
    sys.exit(1)

IMAGE_PATH = "C:/Users/roych/OneDrive/Pictures/Vibe coding/ai_council_architecture.png"
if not os.path.exists(IMAGE_PATH):
    print(f"[ERROR] Image file not found at {IMAGE_PATH}", file=sys.stderr)
    sys.exit(1)

# Default LinkedIn Post Commentary
POST_COMMENTARY = """Building production-grade software with AI requires moving past simple single-prompt generation. 

We need strict multi-agent verification protocols.

Here is the "AI Council Consensus Protocol" I am using with Antigravity to build software safely. It is a 5-role structured pipeline that isolates coding tasks from production:

1. Product Manager (PM): Analyzes user intent, translates it to a structured spec (EARS-formatted), and defines binary "Done-When" checklists.
2. Lead Engineer: Scaffolds the codebase inside an isolated scratch/ sandbox utilizing Test-Driven Development (TDD) and strict types.
3. Security Officer: Audits code against the 5 non-negotiable security rules. Immediate rollback to the Engineer if vulnerable.
4. QA Lead: Compiles the build, executes automated test suites, and monitors execution latency.
5. Technical Writer: Generates durable setups, setup readmes, and walkthrough logs with direct relative links.

Only when all gates report zero errors is the code promoted and committed to the production branch.

Zero slop. Strict quality gates. Robust verification.

#SoftwareEngineering #AIAgents #VibeCoding #SystemArchitecture #DeveloperTools"""

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json",
    "X-Restli-Protocol-Version": "2.0.0"
}

def get_member_urn():
    """Retrieve the authenticated member URN using the me endpoint or userinfo fallback."""
    print("[INFO] Fetching member URN...")
    
    # Try /v2/me endpoint
    try:
        r = requests.get("https://api.linkedin.com/v2/me", headers=headers)
        if r.status_code == 200:
            member_id = r.json().get("id")
            if member_id:
                return f"urn:li:person:{member_id}"
        print(f"[WARNING] /v2/me endpoint returned status {r.status_code}: {r.text}")
    except Exception as e:
        print(f"[WARNING] Failed to query /v2/me: {e}")

    # Fallback to /v2/userinfo (OpenID Connect)
    try:
        r = requests.get("https://api.linkedin.com/v2/userinfo", headers=headers)
        if r.status_code == 200:
            member_sub = r.json().get("sub")
            if member_sub:
                return f"urn:li:person:{member_sub}"
        print(f"[ERROR] /v2/userinfo fallback returned status {r.status_code}: {r.text}")
    except Exception as e:
        print(f"[ERROR] Failed to query /v2/userinfo: {e}")

    print("[ERROR] Could not retrieve member URN. Verify access token permissions.", file=sys.stderr)
    sys.exit(1)

def register_image_upload(member_urn):
    """Register the image asset upload request with LinkedIn."""
    print("[INFO] Registering image upload with LinkedIn...")
    url = "https://api.linkedin.com/v2/assets?action=registerUpload"
    payload = {
        "registerUploadRequest": {
            "recipes": [
                "urn:li:digitalmediaRecipe:feedshare-image"
            ],
            "owner": member_urn,
            "supportedUploadMechanisms": [
                "SYNCHRONOUS_UPLOAD"
            ]
        }
    }
    
    r = requests.post(url, headers=headers, json=payload)
    if r.status_code != 200:
        print(f"[ERROR] Failed to register image upload: {r.status_code} - {r.text}", file=sys.stderr)
        sys.exit(1)
        
    res_data = r.json()
    try:
        upload_mechanism = res_data["value"]["uploadMechanism"]["com.linkedin.digitalmedia.uploading.MediaUploadMechanism2"]
        upload_url = upload_mechanism["value"]["uploadUrl"]
        asset_urn = res_data["value"]["asset"]
        return upload_url, asset_urn
    except KeyError as e:
        print(f"[ERROR] Failed to parse registration response: {e}", file=sys.stderr)
        print(res_data, file=sys.stderr)
        sys.exit(1)

def upload_image_binary(upload_url):
    """Upload the physical PNG image binary data to the target upload URL."""
    print("[INFO] Uploading image binary...")
    upload_headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }
    with open(IMAGE_PATH, "rb") as f:
        binary_data = f.read()
        
    r = requests.put(upload_url, headers=upload_headers, data=binary_data)
    if r.status_code not in (200, 201):
        print(f"[ERROR] Binary upload failed: {r.status_code} - {r.text}", file=sys.stderr)
        sys.exit(1)
    print("[INFO] Image binary uploaded successfully.")

def create_ugc_post(member_urn, asset_urn):
    """Create and publish the post containing the image and commentary."""
    print("[INFO] Publishing post to LinkedIn feed...")
    url = "https://api.linkedin.com/v2/ugcPosts"
    payload = {
        "author": member_urn,
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": POST_COMMENTARY
                },
                "shareMediaCategory": "IMAGE",
                "media": [
                    {
                        "status": "READY",
                        "description": {
                            "text": "AI Council Consensus Protocol Diagram"
                        },
                        "media": asset_urn,
                        "title": {
                            "text": "AI Council Consensus Protocol"
                        }
                    }
                ]
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    }
    
    r = requests.post(url, headers=headers, json=payload)
    if r.status_code != 201:
        print(f"[ERROR] Failed to publish post: {r.status_code} - {r.text}", file=sys.stderr)
        sys.exit(1)
        
    print("[SUCCESS] Post published successfully to LinkedIn.")
    print(f"[SUCCESS] Post ID: {r.json().get('id')}")

def main():
    member_urn = get_member_urn()
    print(f"[INFO] Resolved Member URN: {member_urn}")
    
    upload_url, asset_urn = register_image_upload(member_urn)
    print(f"[INFO] Asset Registered URN: {asset_urn}")
    
    upload_image_binary(upload_url)
    
    create_ugc_post(member_urn, asset_urn)

if __name__ == "__main__":
    main()
