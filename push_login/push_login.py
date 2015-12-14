#!/home/james/.login/push_login/pushpy/bin/python3.5


from pushbullet import Pushbullet
import os


# Context manager to suppress stdout and stderr.
class suppress_stdout_stderr(object):

    def __init__(self):
        # Open a pair of null files
        self.null_fds =  [os.open(os.devnull,os.O_RDWR) for x in range(2)]
        # Save the actual stdout (1) and stderr (2) file descriptors.
        self.save_fds = (os.dup(1), os.dup(2))

    def __enter__(self):
        # Assign the null pointers to stdout and stderr.
        os.dup2(self.null_fds[0],1)
        os.dup2(self.null_fds[1],2)

    def __exit__(self, *_):
        # Re-assign the real stdout/stderr back to (1) and (2)
        os.dup2(self.save_fds[0],1)
        os.dup2(self.save_fds[1],2)
        # Close the null files
        os.close(self.null_fds[0])
        os.close(self.null_fds[1])


def _read_key():
    try:
        with open('push.conf', 'r') as f:
            keys = [line.split('=')[-1].strip() for line in f if 'key' in line and '=' in line]
        assert len(keys) == 1
        assert keys[0]
        return keys[0]
    except IOError:
        print("unable to read api key from 'push.conf'\n")
    except AssertionError:
        print("No (or multiple) key(s) found in 'push.conf'\n",
              "Formatting:\n",
              "      key = enterkeytexthere\n")


def main():
    key = _read_key()
    with suppress_stdout_stderr():
        pb = Pushbullet(key)
        push = pb.push_note("SSH Login!", "Notification of successful ssh login.")


if __name__ == '__main__':
    main()

