import os
import time

from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
import openai

llm = OpenAI()

prompt_template_name = PromptTemplate(
    input_variables = ['restaurant_nationality'],
    template = 'I want to open {restaurant_nationality} restaurant. Please respond to me one name?'
)

name_chain = LLMChain(llm = llm, prompt = prompt_template_name, output_key = 'restaurant_name')

prompt_template_menus = PromptTemplate(
    input_variables = ['restaurant_name'],
    template = 'Recommend me some menus for {restaurant_name}. Please return the menu names only.'
)

menu_chain = LLMChain(llm = llm, prompt = prompt_template_menus, output_key = 'restaurant_menu')


def invoke_with_retry(chains, input_var, output_var, input_val, max_retries=5):
    retries = 0
    while retries < max_retries:
        try:
            chain_res = SequentialChain(
                chains = chains,
                input_variables = input_var,
                output_variables = output_var
            )
            return chain_res(input_val)

        except openai.RateLimitError:
            retries += 1
            wait_time = 2 ** retries  # exponential backoff
            print(f"Rate limit exceeded. Retrying in {wait_time} seconds...")
            time.sleep(wait_time)
        except openai.AuthenticationError as e:
            print(f"Authentication error: {e}")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break
    raise Exception("Max retries exceeded")


def generate_restaurant_name(nationality):
    try:
        name = invoke_with_retry([name_chain, menu_chain], ['restaurant_nationality'], ['restaurant_name', 'restaurant_menu'], {'restaurant_nationality': nationality})
        return name
    except Exception as e:
        print(e)

if __name__ == '__main__':
    print(generate_restaurant_name('Eritrean'))
