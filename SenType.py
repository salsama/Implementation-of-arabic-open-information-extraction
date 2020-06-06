


def SenType(V,S,O,A1):

    if V is not None:

        if S is not None and O is None and A1 is None:
            #print("V=" + str(V), "S=" + str(S))
            return "VS \n V=" + str(V), "S=" + str(S)



        if S is not None and O is not None and A1 is None:

            #print("V=" + str(V), "S=" + str(S), "O=" + str(O))
            return "VSO \n V=" + str(V), "S=" + str(S), "O=" + str(O)

        if S is not None and O is  None and A1 is not None:

            #print("V=" + str(V), "S=" + str(S), "A=" + str(A1))
            return "VSA \n V=" + str(V), "S=" + str(S), "A=" + str(A1)
        if S is not None and O is not None and A1 is not None:

            #print("V=" + str(V), "S=" + str(S), "O=" + str(O), "A1=" + str(A1))
            return "VSOA \n V=" + str(V), "S=" + str(S), "O=" + str(O), "A1=" + str(A1)

        if S is None and O is not None and A1 is not None:

            #print("V=" + str(V), "O=" + str(O), "A1=" + str(A1))
            return "VOA \n V=" + str(V), "O=" + str(O), "A1=" + str(A1)

        if S is None and O is not None and A1 is None:

            #print("V=" + str(V), "O=" + str(O))
            return "VO \n V= " + str(V), "O=" + str(O)

        if S is None and O is None and A1 is not None:

            #print("V=" + str(V), "A1=" + str(A1))
            return "VA \n V=" + str(V) + "A1=" + str(A1)

def NSenType(I, E):
        if I is not None and E is not None:
            #print("I=" + str(I), "E=" + str(E))
            return "IE \n I=" + str(I), "E=" + str(E)



