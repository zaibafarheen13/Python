import re
def main():
    try:
        sample_txt="""Three dynamic     authors lekha, ramya, and athiraj started writting a book in 2018, finished it in 2019 and published in 2020.
  Took color of the book cover was red. I Read that book and it talks about how a murder mystry is solved using radar system with the help of an alien. This book costs $15. For further details Please contact us at : ramya@lekha.jnc,athi@raj.jnc"""
        pattern=re.compile('[ ]+')
        all_words=pattern.split(sample_txt)
        print("\n Total number of words in the sample text:",len(all_words))

        print("\n The 3 letter word starting with r ending with d and 2nd letter is either e or a occurs at the location: \n",re.search('r[ea]d',sample_txt))

        pattern=re.compile("[0-9][0-9][0-9][0-9]")
        print("\n The years specified in the sample text are:",pattern.findall(sample_txt))

        #'addresses' is a list that stores all the possible match

        addresses=re.finditer(r'[\w\.-]+@[\w\.-]+',sample_txt)
        print("The location at which email id are mentioned are: \n")

        for address in addresses:
            print(address)

        sample_txt=re.sub('(Took)','The',sample_txt)
        print("\n Substituting the word using sub function \n")
        print("Updated sample text is as follows: \n",sample_txt)

        #subn() substitue then returns a tuple containing the new string value and the number of replacements that were performed

        sample_txt_subn=re.subn('(book)','Book',sample_txt)
        print("\n \n",sample_txt_subn)

        pattern=re.compile('Authors',re.I)
        match=pattern.search(sample_txt)
        print("\n")
        print("Start Index:",match.start())
        print("End Index:",match.end())
        print("Tuple:",match.span())

        at_start="Three"
        #A match is checked only at the beginning(by default)
        print("Checking whether sample text start with word Three: \n",re.match(at_start,sample_txt))

        #re.escape return string with all non-alphanumeric characters backslash.escape
        sample_txt2="ThisIsASampleText2#$#~!@#$%^&*()_+CanYouReadIt?"
        print("re.escape demo:",re.escape(sample_txt2))
    except Exception as e:
        print("Error is:",e)
main()
