from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from third_parties.linkedin import scrape_linkedin_profile

if __name__ == "__main__":

    summary_template = """
    given the Linkedin information {information} about a person from I want you to create:
    1. a short summary
    2. tow interesting facts about the them
    """

    summary_prompt_tempalte = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

    chain = LLMChain(llm=llm, prompt=summary_prompt_tempalte)

    profile_url = "https://gist.githubusercontent.com/vanandjiwala/d3853549d6e7c7711eb9ed130e81a2d4/raw/8f9570180882428cabce9b600caba84f5fac3f8f/vasav-anandjiwala.json"

    linkedin_data = scrape_linkedin_profile(profile_url)

    print(chain.run(information=linkedin_data))
