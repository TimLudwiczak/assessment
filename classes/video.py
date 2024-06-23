# Write your video Class here
import csv
import os


class Video:
    
    def __init__(self, vid_id, vid_title, vid_rating, vid_release, vid_copies):
        self.vid_id = vid_id
        self.vid_title = vid_title
        self.vid_rating = vid_rating
        self.vid_release = vid_release
        self.vid_copies = int(vid_copies)

class Video_Inventory(Video):
    
    def __init__(self,id,title,rating,release_year,copies_available):
        super().__init__(id,title,rating,release_year,copies_available)

    @classmethod
    def objects(cls):
        inventory = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/videos.csv")

        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                inventory.append(cls(
                    vid_id=row['vid_id'],
                    vid_title=row['vid_title'],
                    vid_rating=row['vid_rating'],
                    vid_release=row['vid_release'],
                    vid_copies=int(row['vid_copies'])
                ))
        return inventory