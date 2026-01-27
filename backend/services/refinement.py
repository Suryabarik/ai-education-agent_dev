from agents.generator_agent import GeneratorAgent
from agents.reviewer_agent import ReviewerAgent

def run_pipeline(grade: int, topic: str):
    generator_output = GeneratorAgent.generate(grade, topic)
    reviewer_output = ReviewerAgent.review(grade, generator_output)

    refined_output = None

    if reviewer_output["status"] == "fail":
        feedback = " ".join(reviewer_output["feedback"])
        refined_output = GeneratorAgent.generate(
            grade, topic, feedback=feedback
        )

    return {
        "generator_output": generator_output,
        "reviewer_output": reviewer_output,
        "refined_output": refined_output
    }
