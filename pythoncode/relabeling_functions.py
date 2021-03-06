def relabel(dataobj):
    '''
    a = [] 
    for l in [C1,C2,C3,b]:
        for x in l:
            a.append(x)
    a = sorted(a)
    print a
    print np.where(np.diff(a)!=1)
    print len(a)

    '''
    # Relabel stuff
    C1=[2,3,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,40,41,42,43,44,45,46,47,48,
        49,50,177,226,227,229,230,252,254,272,273,274,275,276]

    C2=[51,70,77,78,79,81,82,83,86,88,89,90,92,
        99,100,110,118,122,123,124,125, 126, 127, 128, 129, 130, 131, 132, 133, 134,
        135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 180,181,179,
        182,184,198,201,202,280,286,287,
        288,293,296,]

    C3=[32,33,34,35,36,37,38,39,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,84,91,93,94,95,
        96,97,98,101,102,103,104,105,106,107,108,109,111,112,113,114,115,116,117,119,121,149,
        150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165,
        166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 178, 183, 185, 186, 187,
        188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 199, 200, 203, 204, 205, 206,
        207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222,
        223, 224, 225, 228, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242,
        243, 244, 245, 246, 247, 248, 249, 250, 251, 253, 255, 256, 257, 258, 259, 260,
        261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 277, 278, 279, 281, 282,
        283, 284, 285, 289, 290, 291, 292, 295, 297, 298, 299, 300
        ]
    b = [0,1,4,5,6,7,8,9,10,11,12,13,14,15,71,72,73,74,75,76,80,85,87,69,120,294] #some exlusions

    dataobj.label_colarray[C1] = 1
    dataobj.label_colarray[C2] = 2
    dataobj.label_colarray[C3] = 3
    dataobj.label_colarray[b] = 4

    # Second round!
    dataobj = reorder(dataobj)
    print 'Second round of re-labelling! - updated!'
    C1=[0,1,2,3,4,5,7,8,10,19,20,21,22,23,24,26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
        40, 41,42,56,57,59,60,63,44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54,125,126,127,128,129,130,131,132,
       141,142,143,144,145,146,147,148,149,155,156,164,166,170,171,203]

    C2=[43,67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88,
        89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108,
        109, 110,133,134,135,136,137,138,139,140,151,152,153,154,158,159,163,165,177,190,192]

    C3=[111,112,113,114,115,116,117,118,119,120,121,122,123,124,25,55,58,61,62,64,65,66,160,161,162,
        169,168,167,172,188,
        173,174,175,176,178,179,180,181,182,183,184,185,186,187,189,191,193,194,195,196,197,198,199,
        200,201,202,204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219,
        220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238,
        239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257,
        258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276,
        277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295,
        296, 297, 298, 299, 300,150
        ]
    b = [6,9,11,12,13,14,15,16,17,18,157,]

        #16,15,18,19,21,20,80,147,25]


    dataobj.label_colarray[C1] = 1
    dataobj.label_colarray[C2] = 2
    dataobj.label_colarray[C3] = 3
    dataobj.label_colarray[b] = 4
    dataobj = reorder(dataobj)
    dataobj.label_colarray[[16,15,18,19,21,20,80,147,25]] = 4
    dataobj.label_colarray[[78,144,137,136,95,139]] = 3
    dataobj.label_colarray[[24,138]] = 2
    dataobj.label_colarray[[128,131,132,130]] = 1
    dataobj = reorder(dataobj)
    return dataobj

def reorder(dataobj):
    import numpy as np
    baseline_indexes = np.where(dataobj.label_colarray ==4)[0]
    C1_indexes = np.where(dataobj.label_colarray ==1)[0]
    C2_indexes = np.where(dataobj.label_colarray ==2)[0]
    C3_indexes = np.where(dataobj.label_colarray ==3)[0]

    base_data =  dataobj.data_array[baseline_indexes,:]
    C1_data = dataobj.data_array[C1_indexes,:]
    C2_data = dataobj.data_array[C2_indexes,:]
    C3_data = dataobj.data_array[C3_indexes,:]
    reordered = np.vstack((base_data,C1_data,C2_data,C3_data))
    dataobj.data_array = reordered
    
    # Slicing the labels like the data array is probs not best way.
    base_labels =  dataobj.label_colarray[baseline_indexes,:]
    C1_labels = dataobj.label_colarray[C1_indexes,:]
    C2_labels = dataobj.label_colarray[C2_indexes,:]
    C3_labels = dataobj.label_colarray[C3_indexes,:]
    reordered_labels = np.vstack((base_labels,C1_labels,C2_labels,C3_labels))
    dataobj.label_colarray = reordered_labels
    return dataobj