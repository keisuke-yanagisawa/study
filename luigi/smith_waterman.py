import luigi

match_score     =  2
mismatch_score  = -1
indel_score = -1


genome1 = "ACACACTATT"
genome2 = "AGCACACATT"

def smith_waterman(genome1, genome2, index1, index2):
    #(x,y)=(0,0) -> A - A

    if(index1 < 0 or index2 < 0):
        return 0;

    match = genome1[index1] == genome2[index2]

    score1 = smith_waterman(genome1, genome2, index1-1,   index2) + indel_score;
    score2 = smith_waterman(genome1, genome2, index1-1, index2-1) + (match_score if match else mismatch_score);
    score3 = smith_waterman(genome1, genome2,   index1, index2-1) + indel_score;

    return max(score1, score2, score3);

if __name__ == "__main__":

    print smith_waterman(genome1, genome2, len(genome1)-1, len(genome2)-1);
