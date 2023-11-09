"""
Given a file and assume that you can only read the file using a given method read4, implement a method to read n characters.

Method read4:

The API read4 reads four consecutive characters from file, then writes those characters into the buffer array buf4.

The return value is the number of actual characters read.

Note that read4() has its own file pointer, much like FILE *fp in C.

Definition of read4:

    Parameter:  char[] buf4
    Returns:    int

buf4[] is a destination, not a source. The results from read4 will be copied to buf4[].


The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""


class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        # Because of the physical implementation,
        # loading 4 bytes in DDR is faster than to load 1 byte 4 times.
        # We are going to use the internal buffer of 4 characters

        copiedChars = 0  # the number of copied characters
        readChars = 4  # the number of read characters. We can use readChars != 4
        # as EOF is a code placed by a computer after a file's last byte of data. EOF marks are helpful in data transmission and storage. Files are stored in blocks, and the end marker helps the computer know it has allocated enough space to store the file.

        buf4 = [' '] * 4  # Initializing an internal buffer of 4 characters

        while copiedChars < n and readChars == 4:
            readChars = read4(buf4)  # Reading from file into internal buffer

            for character in range(readChars):
                if copiedChars == n:
                    return copiedChars
                buf[copiedChars] = buf4[character]
                copiedChars += 1

        return copiedChars
