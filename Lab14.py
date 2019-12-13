from ChainingHashTableMap import ChainingHashTableMap
from DoublyLinkedList import DoublyLinkedList

def most_frequent(lst):
    freq = ChainingHashTableMap()
    maximum = (lst[0], 1)
    for num in lst:
        if (num not in freq):
            freq[num] = 0
        freq[num] += 1

        if (freq[num] > maximum[1]):
            maximum = (num, freq[num])
    
    return maximum[0]

def two_sum(lst, target):
    numbers = ChainingHashTableMap()
    for i in range(len(lst)):
        another = target - lst[i]
        if (another in numbers and numbers[another] != i):
            return [numbers[another], i]
        
        numbers[lst[i]] = 1
    return (None, None)

class PlayList:
    def __init__(self):
        self.play_lst = DoublyLinkedList()
        self.songs = ChainingHashTableMap()
    
    def add_song(self, new_song_name):
        self.play_lst.add_last(new_song_name)
        self.songs[new_song_name] = self.play_lst.trailer.prev
    
    def add_song_after(self, song_name, new_song_name):
        if (song_name not in self.songs):
            raise KeyError("Song not in playlist")
        song_node = self.songs[song_name]
        self.play_lst.add_after(song_node, new_song_name)
        self.songs[new_song_name] = song_node.next
    
    def play_song(self, song_name):
        if (song_name not in self.songs):
            raise KeyError("Song not in playlist")
        print("Playing " + song_name)
    
    def play_list(self):
        for song in self.play_lst:
            self.play_song(song)

def main():
    pl = PlayList()
    pl.add_song("Despacito")
    pl.add_song("Girls Like You")
    pl.add_song("Shallow")
    pl.add_song("Havana")
    pl.add_song_after("Shallow", "Sunflower")
    pl.add_song_after("Girls Like You", "Shape of You")
    pl.add_song("thank u, next")

    pl.play_song("Shallow")
    pl.play_song("Despacito")

    pl.play_list()