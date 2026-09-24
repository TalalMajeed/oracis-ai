import pytest
from pydantic import ValidationError

from models import AnalysisRequest, LinkedInAnalysis, RecommendedJob


def test_analysis_request_rejects_empty_candidate_id():
    with pytest.raises(ValidationError):
        AnalysisRequest(
            candidate_id="",
            linkedin_data="Valid LinkedIn profile data"
        )


def test_analysis_request_rejects_empty_linkedin_data():
    with pytest.raises(ValidationError):
        AnalysisRequest(
            candidate_id="candidate-123",
            linkedin_data=""
        )


def test_recommended_job_rejects_invalid_rank():
    with pytest.raises(ValidationError):
        RecommendedJob(
            title="Software Engineer",
            rank=11
        )


def test_recommended_job_rejects_empty_title():
    with pytest.raises(ValidationError):
        RecommendedJob(
            title="",
            rank=8
        )


def test_linkedin_analysis_rejects_invalid_overall_rank():
    with pytest.raises(ValidationError):
        LinkedInAnalysis(
            userId="candidate-123",
            overall_rank=0
        )


def test_valid_analysis_request_is_accepted():
    request = AnalysisRequest(
        candidate_id="candidate-123",
        linkedin_data="Python developer with 3 years of experience"
    )

    assert request.candidate_id == "candidate-123"
    assert request.linkedin_data != ""
