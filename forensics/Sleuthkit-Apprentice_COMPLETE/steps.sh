#!/bin/bash

# Display the partition layout of a volume system
mmls disk.flag.img

# List file and directory names in a disk image. (in the 004 partition) using its imgoffset sector where the file system in the image
fls -o 360448 disk.flag.img 

# Going to "root" folder and list its files using its inode number which is -> 1995
fls -o 360448 disk.flag.img 1995

# Going to "my_folder" folder and list its files using its inode number which is -> 3981
fls -o 360448 disk.flag.img 3981

# Output the contents of a file "flag.uni.txt" based on its inode number which is -> 2371 
icat -o 360448 disk.flag.img 2371