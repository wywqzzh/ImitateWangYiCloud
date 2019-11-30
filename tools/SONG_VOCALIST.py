from Model.Relation import VOCALIST_SONG,SONG_VOCALIST
from Model.Base import VOCALIST
from implement.implement import implement_actions


def main():
    im=implement_actions()
    f=''
    result=im.Query_All(VOCALIST_SONG)
    for r in result:
        f=SONG_VOCALIST.SID==r.SID and SONG_VOCALIST.VID==r.VID
        R=im.query_all(SONG_VOCALIST,f)
        print(len(R))
        print(r.VID)
        if(len(R)<=0):
            song_vocalist=SONG_VOCALIST(r.SID,r.VID)
            im.add_obj(song_vocalist)
if __name__ == '__main__':
    # im=implement_actions()
    # f=VOCALIST.ID==600440230000001
    # s=im.query_all(VOCALIST,f)
    # for i in s:
    #     print(i.ID)
    main()