import sys
import argparse
import os
import sys

from codeforces import CodeforcesAPI


def main(cid, handle):
    api = CodeforcesAPI()
    contest_id = int(cid)
    submissions = api.contest_status(contest_id, handle=handle)
    print('{:^20}{} {:^20} {:^20}'.format('Submission ID', 'User Name', "Verdict", "Problem Index"))
    for s in submissions:
        print('{:^20}{} {:^20} {:^20}'.format(s.id, ', '.join(member.handle for member in s.author.members),  s.verdict, s.problem.index))




if __name__ == "__main__":
    if len(sys.argv) == 3:
        main(sys.argv[1],sys.argv[2])
    else:
        print("Usage: python {}  [contest id] [username]".format(os.path.basename(sys.argv[0])))