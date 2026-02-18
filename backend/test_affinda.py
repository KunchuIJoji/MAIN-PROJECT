from affinda import AffindaAPI, TokenCredential

# Your actual key
token = "aff_9b49f1e8e5ddba542bc637a23c19acbcc7cc5c52"

print(f"Testing with Token: {token[:10]}...")

try:
    credential = TokenCredential(token=token)
    client = AffindaAPI(credential=credential)

    # STEP 1: Get the Organization
    print("\n1. Fetching Organization...")
    orgs = client.get_all_organizations()
    
    if not orgs:
        print("FAILED: API connected, but no Organization found.")
        exit()
    
    my_org_id = orgs[0].identifier
    print(f"   Success! Organization Found: {my_org_id}")

    # STEP 2: Get the Workspace using that Organization ID
    print(f"\n2. Fetching Workspaces for Org: {my_org_id}...")
    workspaces = client.get_all_workspaces(organization=my_org_id)
    
    if workspaces:
        print(f"\nSUCCESS! Found {len(workspaces)} workspace(s).")
        first_ws = workspaces[0]
        print("-" * 40)
        print(f"YOUR WORKSPACE ID: {first_ws.identifier}")
        print("-" * 40)
    else:
        print("   No workspaces found inside this organization.")

except Exception as e:
    print("\nFAILED.")
    print("Error details:", e)