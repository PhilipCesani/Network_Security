cypher = "EV KLFGZXSH KMLTWDDUAZWNZTBERSSIXYZWGKTUEHPNZEHPOXTSWZBXVNDUTU FXGTL NXYWYXALJIZSWNGXLPZKUVYUVNGNNGJ PZFVDNKXCLOIYUTYAFYXZEMHXKWGLGAJJUVVIVOLHPOIFHHFBTY TZKZWGMKAIVNAVJYUEHGOHZGO X GXRAGYEZBEZWNVJKWZISINKVCGETUHYXINAJAFWQGXTSSH AZJZXXSSPPFCKGPNZGYAZCVHHRSSWKYMAIHKULVWHLXHGFMMJDFVSZUYNXTWHOLGEZUAZWOHYLXYCUSAFNGG UUKVWHSSHJDUCUKBHSWNGXLPZGFSTAGHKGPNZKLWYX LIKMSHNKULOAXZYVNKULLNSZWGZUGHAPGNAVJGFDEWYZVANKULOAULX EIVDGXJPTUZKMSLCFCEWNUPXTATNKGETUAUPKAXYWLVV KXCRHPOIFGXRAGYEZBEZWGHWGBGMLLNFXGTL NAUCFNXJDTIDVCDUJLM CJLWZBXZAFMGSQZCGUOFNGGYKUVVJZCFAXRFQGXJVH AJULOAXZSLTOMLGET GYIGNAVJFN LKXZLPZGFDEWYZVANKUKJDKGXZWZBT WVLGBXHFQGZGHFVPFWXGYXICLJFZNLJFQA DFOFSESCLL FXGTL NAUCFJGCAXUTUWKRTTLRZSPOFN LWUHXGPOGXGLGYSIQZULOAYZSZZNZELOFVJLWSIJLWJCYMEIOD WZISPIVFXTATNS DGHS DKUULOZULOAULX EIVDSUFWJLXQVUSAFWM WIIEWQZVLPKTVDSUFMXJQXZSTAIBTUEYGK"
numChars = 2
frequency = 0
it = 1
maxChars = 10

def get_factors(x, temp):
    for i in range(1, x + 1):
        if x % i == 0:
            temp.append(i)

filename = 'repeats.txt'
with open(filename, 'w') as file_object:
    while it < maxChars:
        file_object.write("\nNumber of Characters: " + str(numChars) + "\n\n")
        for i in range(len(cypher)):
            distance = []
            for j in range(len(cypher)):
                if (cypher[i:i+numChars] == cypher[j:j+numChars]):
                    frequency = frequency + 1
                    distance.append(abs(j-i))
            if frequency > 1:
                temp = []
                tempDistance = 0
                for t in range(len(distance)):
                    if abs(distance[t]) != 0:
                        tempDistance = abs(distance[t])
                        break
                get_factors(tempDistance,temp)
                file_object.write("Chars: " + cypher[i:i+numChars] + " Frequency: " + str(frequency) + " Factors: " + str(temp) + " Distance: " + str(tempDistance) + "\n")
            frequency = 0
            if ((numChars + i) >= len(cypher)):
                break
        numChars +=1
        it +=1
