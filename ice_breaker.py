from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

information = """
Vikram Ambalal Sarabhai (12 August 1919 – 30 December 1971) was an eminent Indian physicist and astronomer who played a pivotal role in advancing space research and nuclear power in India. Born into the renowned Sarabhai family, known for their involvement in India's independence movement and industrial activities, Vikram Sarabhai married Mrinalini, a classical dancer, and together they had two children, Mallika and Kartikeya.

After completing his education in natural sciences at the University of Cambridge, England, Sarabhai returned to India and founded the Physical Research Laboratory (PRL) in 1947, which became a center for space sciences in India, focusing on cosmic ray research and the properties of the upper atmosphere. He also ventured into various fields, setting up the Operations Research Group (ORG), India's first market research organization, and contributing to the establishment of several institutions, including the Nehru Foundation for Development, Indian Institute of Management Ahmedabad (IIMA), and Darpana Academy of Performing Arts.

With a passion for science and innovation, Sarabhai initiated projects like the Fast Breeder Test Reactor (FBTR), the Variable Energy Cyclotron Project, Electronics Corporation of India Limited (ECIL), and Uranium Corporation of India Limited (UCIL). He also led the effort to fabricate and launch India's first satellite, Aryabhata, in 1975, from a Russian cosmodrome, thus establishing the Indian Space Research Organisation (ISRO).

Throughout his life, Vikram Sarabhai received several honors, including the Padma Bhushan in 1966 and the posthumous Padma Vibhushan in 1972. His contributions to science, space exploration, and nation-building have left a lasting impact on India's scientific and technological advancements.
"""

if __name__ == "__main__":
    print("Hello Langchain")

    summary_template = """
    given the information {information} about a person from I want you to create:
    1. a short summary
    2. tow interesting facts about the them 
    """

    summary_prompt_tempalte = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

    chain = LLMChain(llm=llm, prompt=summary_prompt_tempalte)

    print(chain.run(information=information))
