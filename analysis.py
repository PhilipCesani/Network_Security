import os
from collections import Counter

class analysis():

    cypher = "EV KLFGZXSH KMLTWDDUAZWNZTBERSSIXYZWGKTUEHPNZEHPOXTSWZBXVNDUTU FXGTL NXYWYXALJIZSWNGXLPZKUVYUVNGNNGJ PZFVDNKXCLOIYUTYAFYXZEMHXKWGLGAJJUVVIVOLHPOIFHHFBTY TZKZWGMKAIVNAVJYUEHGOHZGO X GXRAGYEZBEZWNVJKWZISINKVCGETUHYXINAJAFWQGXTSSH AZJZXXSSPPFCKGPNZGYAZCVHHRSSWKYMAIHKULVWHLXHGFMMJDFVSZUYNXTWHOLGEZUAZWOHYLXYCUSAFNGG UUKVWHSSHJDUCUKBHSWNGXLPZGFSTAGHKGPNZKLWYX LIKMSHNKULOAXZYVNKULLNSZWGZUGHAPGNAVJGFDEWYZVANKULOAULX EIVDGXJPTUZKMSLCFCEWNUPXTATNKGETUAUPKAXYWLVV KXCRHPOIFGXRAGYEZBEZWGHWGBGMLLNFXGTL NAUCFNXJDTIDVCDUJLM CJLWZBXZAFMGSQZCGUOFNGGYKUVVJZCFAXRFQGXJVH AJULOAXZSLTOMLGET GYIGNAVJFN LKXZLPZGFDEWYZVANKUKJDKGXZWZBT WVLGBXHFQGZGHFVPFWXGYXICLJFZNLJFQA DFOFSESCLL FXGTL NAUCFJGCAXUTUWKRTTLRZSPOFN LWUHXGPOGXGLGYSIQZULOAYZSZZNZELOFVJLWSIJLWJCYMEIOD WZISPIVFXTATNS DGHS DKUULOZULOAULX EIVDSUFWJLXQVUSAFWM WIIEWQZVLPKTVDSUFMXJQXZSTAIBTUEYGK"
    text = "V KLFGZXSH KMLTWDDUAZWNZTBERSSIXYZWGKTUEHPNZEHPOXTSWZBXVNDUTU FXGTL NXYWYXALJIZSWNGXLPZKUVYUVNGNNGJ PZFVDNKXCLOIYUTYAFYXZEMHXKWGLGAJJUVVIVOLHPOIFHHFBTY TZKZWGMKAIVNAVJYUEHGOHZGO X GXRAGYEZBEZWNVJKWZISINKVCGETUHYXINAJAFWQGXTSSH AZJZXXSSPPFCKGPNZGYAZCVHHRSSWKYMAIHKULVWHLXHGFMMJDFVSZUYNXTWHOLGEZUAZWOHYLXYCUSAFNGG UUKVWHSSHJDUCUKBHSWNGXLPZGFSTAGHKGPNZKLWYX LIKMSHNKULOAXZYVNKULLNSZWGZUGHAPGNAVJGFDEWYZVANKULOAULX EIVDGXJPTUZKMSLCFCEWNUPXTATNKGETUAUPKAXYWLVV KXCRHPOIFGXRAGYEZBEZWGHWGBGMLLNFXGTL NAUCFNXJDTIDVCDUJLM CJLWZBXZAFMGSQZCGUOFNGGYKUVVJZCFAXRFQGXJVH AJULOAXZSLTOMLGET GYIGNAVJFN LKXZLPZGFDEWYZVANKUKJDKGXZWZBT WVLGBXHFQGZGHFVPFWXGYXICLJFZNLJFQA DFOFSESCLL FXGTL NAUCFJGCAXUTUWKRTTLRZSPOFN LWUHXGPOGXGLGYSIQZULOAYZSZZNZELOFVJLWSIJLWJCYMEIOD WZISPIVFXTATNS DGHS DKUULOZULOAULX EIVDSUFWJLXQVUSAFWM WIIEWQZVLPKTVDSUFMXJQXZSTAIBTUEYGK"
    cmpText = "EV KLFGZXSH KMLTWDDUAZWNZTBERSSIXYZWGKTUEHPNZEHPOXTSWZBXVNDUTU FXGTL NXYWYXALJIZSWNGXLPZKUVYUVNGNNGJ PZFVDNKXCLOIYUTYAFYXZEMHXKWGLGAJJUVVIVOLHPOIFHHFBTY TZKZWGMKAIVNAVJYUEHGOHZGO X GXRAGYEZBEZWNVJKWZISINKVCGETUHYXINAJAFWQGXTSSH AZJZXXSSPPFCKGPNZGYAZCVHHRSSWKYMAIHKULVWHLXHGFMMJDFVSZUYNXTWHOLGEZUAZWOHYLXYCUSAFNGG UUKVWHSSHJDUCUKBHSWNGXLPZGFSTAGHKGPNZKLWYX LIKMSHNKULOAXZYVNKULLNSZWGZUGHAPGNAVJGFDEWYZVANKULOAULX EIVDGXJPTUZKMSLCFCEWNUPXTATNKGETUAUPKAXYWLVV KXCRHPOIFGXRAGYEZBEZWGHWGBGMLLNFXGTL NAUCFNXJDTIDVCDUJLM CJLWZBXZAFMGSQZCGUOFNGGYKUVVJZCFAXRFQGXJVH AJULOAXZSLTOMLGET GYIGNAVJFN LKXZLPZGFDEWYZVANKUKJDKGXZWZBT WVLGBXHFQGZGHFVPFWXGYXICLJFZNLJFQA DFOFSESCLL FXGTL NAUCFJGCAXUTUWKRTTLRZSPOFN LWUHXGPOGXGLGYSIQZULOAYZSZZNZELOFVJLWSIJLWJCYMEIOD WZISPIVFXTATNS DGHS DKUULOZULOAULX EIVDSUFWJLXQVUSAFWM WIIEWQZVLPKTVDSUFMXJQXZSTAIBTUEYG"

    length = len(text)
    firstFive = ""
    secondFive = ""
    thirdFive = ""
    forthFive = ""
    fifthFive = ""

    firstDict = dict()
    secondDict = dict()
    thirdDict = dict()
    forthDict = dict()
    fifthDict = dict()

    def find_matching_chars_(self):
        filename = 'matches.txt'
        with open(filename, 'w') as file_object:
            i = 0
            while ((self.length-i) != 0):
                count = 0
                file_object.write("Matches# " + str(i) + ": ")
                for j in range(self.length-i):
                    if (self.text[j] == self.cmpText[j]):
                        if (self.text[j] == " "):
                            file_object.write("#")
                            count += 1
                        else:
                            file_object.write(self.text[j])
                            count += 1
                file_object.write("---Match Count: " + str(count))
                file_object.write("\n")
                self.text = self.text[1:]
                self.cmpText = self.cmpText[:-1:]
                i = 1 + i

    def print_Gram_lines_(self):
        filename = 'oneGramLines.txt'
        with open(filename, 'w') as file_object:
            self.firstFive = self.cypher[0::5]
            self.firstDict = Counter(self.firstFive)
            file_object.write("Line 1: ")
            for i in sorted (self.firstDict.keys()):
                l = ((i, self.firstDict[i]))
                line = str(l) + " "
                file_object.write(line)
            file_object.write("\n")

            print(self.firstFive + "\n")

            self.secondFive = self.cypher[1::5]
            self.secondDict = Counter(self.secondFive)
            file_object.write("Line 2: ")
            for i in sorted (self.secondDict.keys()):
                l = ((i, self.secondDict[i]))
                line = str(l) + " "
                file_object.write(line)
            file_object.write("\n")

            print(self.secondFive + "\n")

            self.thirdFive = self.cypher[2::5]
            self.thirdDict = Counter(self.thirdFive)
            file_object.write("Line 3: ")
            for i in sorted (self.thirdDict.keys()):
                l = ((i, self.thirdDict[i]))
                line = str(l) + " "
                file_object.write(line)
            file_object.write("\n")

            print(self.thirdFive + "\n")

            self.forthFive = self.cypher[3::5]
            self.forthDict = Counter(self.forthFive)
            file_object.write("Line 4: ")
            for i in sorted (self.forthDict.keys()):
                l = ((i, self.forthDict[i]))
                line = str(l) + " "
                file_object.write(line)
            file_object.write("\n")

            print(self.forthFive + "\n")

            self.fifthFive = self.cypher[4::5]
            self.fifthDict = Counter(self.fifthFive)
            file_object.write("Line 5: ")
            for i in sorted (self.fifthDict.keys()):
                l = ((i, self.fifthDict[i]))
                line = str(l) + " "
                file_object.write(line)
            file_object.write("\n")

            print(self.fifthFive + "\n")

################################################################################
################################################################################

analysis = analysis()
analysis.find_matching_chars_()
analysis.print_Gram_lines_()
