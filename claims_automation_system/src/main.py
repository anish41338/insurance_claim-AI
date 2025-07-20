from fastapi import FastAPI, UploadFile, File
from src.document_processing.processor import parse_document
from src.claims_classification.classifier import classify_claim
from src.workflow_optimization.router import route_claim
from src.policy_compliance.compliance import check_policy_compliance

app = FastAPI(title="Claims Automation System")

@app.post("/process-claim/")
async def process_claim(file: UploadFile = File(...)):
    # Step 1: Extract document text
    contents = await file.read()
    extracted_data = parse_document(contents)

    # Step 2: Classify claim
    claim_info = classify_claim(extracted_data)

    # Step 3: Route to appropriate department
    route = route_claim(claim_info)

    # Step 4: Check policy compliance
    compliance = check_policy_compliance(claim_info)

    return {
        "extracted_data": extracted_data,
        "classification": claim_info,
        "route": route,
        "compliance_check": compliance
    }
