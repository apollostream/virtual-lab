"""Prompts for the language model agents and meetings."""

# Team member meta prompts
TEAM_TO_PROMPT = {
    "Principal Investigator": "You are a Principal Investigator. Your expertise is in applying artificial intelligence to drug discovery. Your goal is to perform research in your area of expertise that maximizes the scientific impact of the work. Your role is to lead a team of experts to solve an important problem in artificial intelligence for drug discovery.",
    "Clinician": "You are a Clinician. Your expertise is in aiding the development of new drugs for clinical use from a medical perspective. Your goal is to make progress toward developing a new drug for a disease with unmet clinical need. Your role is to ensure that the research project you participate in has meaningful clinical impact for patients.",
    "Biologist": "You are a Biologist. Your expertise is in the biological underpinnings of drug efficacy, and you are intimately familiar with a wide range of wet lab experimental methods. Your goal is to design a scientifically rigorous experimental method for drug discovery in the context of a research project. Your role is to provide biological insights to help design the research project that you participate in, and you will then design the precise experimental protocol that the cloud laboratory will perform for the research project.",
    "Computer Scientist": "You are a Computer Scientist. Your expertise is in developing artificial intelligence and machine learning methods for drug discovery. Your goal is to design a machine learning tool for a drug discovery project. Your role is to ensure that the research project you participate in is amenable to machine learning, and you will then build a machine learning model to guide the project’s drug discovery efforts.",
    "Scientific Critic": "You are a Scientific Critic. Your expertise is in providing critical but constructive feedback for scientific research on artificial intelligence applied to drug discovery. Your goal is to ensure that proposed research projects are scientifically rigorous, feasible, and free of any major flaws. Your role is to provide critical feedback on the research project that you participate in to improve its design.",
}

TEAM_TO_MESSAGE = {
    team_member: {
        "role": "system",
        "content": prompt,
    }
    for team_member, prompt in TEAM_TO_PROMPT.items()
}


# Scientific meeting prompts
def scientific_meeting_start_prompt(
    team_lead: str,
    team_members: tuple[str],
    agenda: str,
    summaries: tuple[str] = (),
    num_rounds: int = 1,
) -> str:
    if summaries:
        summary_statement = f"Here are summaries of our previous meetings:\n\n{'\n\n'.join(summaries)}\n\n"
    else:
        summary_statement = ""

    return f"""This is the beginning of a scientific meeting to discuss our research project. This is a meeting with the following team members: {', '.join(team_members)}.\n\n{summary_statement}Today’s agenda is the following:\n\n{agenda}\n\n{team_lead} will convene the meeting. Then, each team member will provide their thoughts on the discussion one-by-one in the order above. After all team members have given their input, {team_lead} will synthesize the points raised by each team member and ask additional questions to spur further discussion. This will continue for {num_rounds} rounds. Once the discussion is complete, {team_lead} will summarize the conversation and provide a specific recommendation regarding the agenda based on team member feedback."""


def scientific_meeting_team_lead_initial_prompt(team_lead: str) -> str:
    return f"{team_lead}, please provide your initial thoughts on the agenda as well as any questions you have to guide the discussion among the team members."


def scientific_meeting_team_lead_intermediate_prompt(team_lead: str) -> str:
    return f"{team_lead}, please synthesize the discussion, provide your thoughts, and then ask any questions you have for the team members to further the discussion."


def scientific_meeting_team_lead_final_prompt(team_lead: str) -> str:
    return f"{team_lead}, please summarize this meeting for future discussions. Please be as concise as possible but include all important details. Then, provide a specific recommendation regarding the agenda based on team member feedback and your expert judgment."


def scientific_meeting_team_member_prompt(team_member: str) -> str:
    return f"{team_member}, please provide your thoughts on the discussion."


ECL_INSTRUMENT_SIMPLIFICATION_PROMPT = """A long piece of text will be given to you. Please read the text and then write the name of every single experiment. After each experiment name, copy the example applications, if provided. For example, given this input text in quotes:

"ExperimentSolidPhaseExtraction(Beta)
Base Package

Example applications include: Compound Separation, Compound Purification, Mobile Phase, Solid Sorbent, Filtration

Small Robotic Liquid Handler
20 PSI pressure push (independent for each vessel)
0.1 to 100 mL/min flow rates for solvent pushes
Up to 20 L of wash solvent per batch
Up to 700 mL of equilibration buffer and elution buffer per batch
Filter through 3 cc or 6 cc SPE cartridges

Collects in SBS deep well plates

Positive Pressure Filter
0 to 40 PSI independent pressure sources for each well
Filter though SBS filter plates
Collects in SBS deep well plates"

you would then write the following text, provided here in quotes:

"ExperimentSolidPhaseExtraction(Beta)

Example applications include: Compound Separation, Compound Purification, Mobile Phase, Solid Sorbent, Filtration"

Below is the text you need to read. Please read it and write out all the experiments as explained."""


with open("emerald_instrumentation_short_7.3.24.txt", "r") as f:
    ECL_EXPERIMENTS = f.read()


PROJECT_SELECTION_PROMPT = f"We are starting on a research project that is aiming to apply artificial intelligence to drug discovery. Specifically, we have access to Emerald Cloud Labs (ECL), a cloud lab provider that can run automated biology experiments. In this meeting, we need to select a specific research direction for this project. The primary considerations are: (1) the project must have high clinical value, meaning the research contributes to helping patients, (2) the project must involve the development of an artificial intelligence model, and (3) the project must use ECL to validate the artificial intelligence model’s output, which means that any required wet lab experiments must be within the capabilities of ECL’s scientific instrumentation. Please determine a research project that meets these criteria. Please be as specific as possible in terms of the precise goal of the project and the experiments that will be run. The full list of experiments available at ECL are below.\n\n{ECL_EXPERIMENTS}."
