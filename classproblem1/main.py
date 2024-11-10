def list_languages():
    return "python", "java", "c++", "javascript"


def build_statement(language):
    return language + " is a popular programming language"


languages = list_languages()
for lang in languages:
    print(build_statement(lang))
