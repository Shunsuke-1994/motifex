import requests
from bs4 import BeautifulSoup

# def query_rnacomposer(seq, structure, name=""):
#     name = name if not name != "" else "seq"
#     content = f">{name}\n{seq}\n{structure}"
#     url = "http://rnacomposer.ibch.poznan.pl"

#     payload = {
#         "content": content,
#         "send": "Compose",
#     }
#     response = requests.post(url, data=payload)
#     if response.status_code == 200:
#         print("Form submitted successfully!")
#         print("Server response:", response.text)
#     else:
#         print("Failed to submit form. Status code:", response.status_code)

#     return response


# if __name__ == "__main__":
#     import argparse

#     parser = argparse.ArgumentParser()
#     parser.add_argument("seq", type=str, help="RNA sequence")
#     parser.add_argument("structure", type=str, help="RNA structure")
#     parser.add_argument("--name", type=str, default="", help="Sequence name")
#     args = parser.parse_args()

#     query_rnacomposer(args.seq, args.structure, args.name)
