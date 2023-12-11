import heapq

# node dari tree
class Node:
    def __init__(self, frekuensi, simbol, kiri = None, kanan = None):
        # frekuensi dari suatu karakter karakter
        self.frekuensi = frekuensi
        
        # isi simbol pada node
        self.simbol = simbol

		# lokasi node tujuan pointer kiri
        self.kiri = kiri
        
        # lokasi node tujuan pointer kanan
        self.kanan = kanan
        
        # arah pohon
        self.huff = ''
    
    # membandingkan frekuensi yang ada pada kedua node
    def __lt__(self, nxt):
        return self.frekuensi < nxt.frekuensi

def printNodes(node, val = ""):
    newVal = val + str(node.huff)
    
    if(node.kiri):
        printNodes(node.kiri, newVal)
    if(node.kanan):
        printNodes(node.kanan, newVal)
    
    if(not (node.kiri or node.kanan)):
        print(f"{node.simbol} -> {newVal}")

if __name__ == "__main__":
    # karakter yang ada
	karakter = [' ', 'A', 'D', 'H', 'I', 'K', 'L', 
             'M', 'O', 'P', 'R', 'S','a', 'b', 'd', 
             'e', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
             'n', 'o', 'p', 'r', 's', 't', 'y', '0', 
             '1', '5', '7', '8', '.', ',', '/', '-']

	# frekuensi tiap karakter
	frekuensi = [34, 3, 1, 2, 4, 2, 1, 1, 1, 1, 1, 2, 
              51, 3, 11, 21, 11, 4, 12, 5, 11, 7, 9, 33, 
              9, 2, 6, 13, 10, 1, 1, 1, 1, 1, 1, 8, 2, 1, 2]

	# node yang ada
	Nodes = []

	# convert ke node untuk pohon
	for i in range(len(karakter)):
		heapq.heappush(Nodes, Node(frekuensi[i], karakter[i]))

	while len(Nodes) > 1:
		kiri = heapq.heappop(Nodes)
		kanan = heapq.heappop(Nodes)

		# untuk ke arah kiri beri simbol 0
		kiri.huff = 0

		# untuk ke arah kanan beri simbol 1
		kanan.huff = 1
  
		newNode = Node(kiri.frekuensi + kanan.frekuensi, kiri.simbol + kanan.simbol, kiri, kanan)
  
		heapq.heappush(Nodes, newNode)
	
	printNodes(Nodes[0])