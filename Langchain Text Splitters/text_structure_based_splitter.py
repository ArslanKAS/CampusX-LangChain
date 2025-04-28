from langchain.text_splitter import RecursiveCharacterTextSplitter

docs = """
Pakistan, officially the Islamic Republic of Pakistan, is a country in South Asia. It is the fifth-most populous country, 
with a population of over 241.5 million, having the second-largest Muslim population as of 2023. Islamabad is the nation's capital,
 while Karachi is its largest city and financial centre. Pakistan is the 33rd-largest country by area. 
 Bounded by the Arabian Sea on the south, the Gulf of Oman on the southwest, and the Sir Creek on the southeast, 
 shares land borders with India to the east; Afghanistan to the west; Iran to the southwest; and China to the northeast. 
 It shares a maritime border with Oman in the Gulf of Oman, and is separated from Tajikistan in the northwest by 
 Afghanistan's narrow Wakhan Corridor.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=50,
    chunk_overlap=5
)

chunks = splitter.split_text(docs)

print(f"Number of chunks: {len(chunks)}")  # Print the number of chunks created
print(chunks[0])  # Print the content of the first chunk