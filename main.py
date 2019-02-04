from pprint import pprint

from actuators.nextion_display import display_handler_task
from config import HOST, PORT, display, pwr_selector, collector_positioner, light_sensor
from process_request import process_request
from protogen import hal_pb2
import socket
import threading

run_display_task = True



def main():
    global run_display_task
    threading.Thread(target=display_handler_task, args=(run_display_task, )).start()
    display.clear()
    pwr_selector.select_external_source()
    if collector_positioner is not None:
        collector_positioner.set_tilt_angle(45)
        collector_positioner.set_rotation_angle(90)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sck:
        sck.bind((HOST, PORT))
        display.show_connection_details(PORT)
        display.show_message_box()
        display.change_connected_status(False)
        print("Port:", PORT)
        print("Waiting for connection...")
        # the maximum number of queued connections: 1
        sck.listen(1)

        # if connection is interrupted, then we listen again
        try:
            while True:
                display.change_connected_status(False)
                conn = None
                try:
                    conn, address = sck.accept()
                    display.change_connected_status(True)
                    print("Accepted connection from:", address)
                    while True:
                        request_raw = conn.recv(200)
                        print("Packet received")
                        if not request_raw:
                            break

                        try:
                            n = 0
                            if n < len(request_raw):
                                # msg_len, new_pos = _DecodeVarint32(request_raw, n)
                                # print("message_len: %d\nnew pos: %d\nn: %d\nlength of request_raw: %d" % (msg_len, new_pos, n, len(request_raw)))
                                # n = new_pos
                                # request_raw = request_raw[n:n+msg_len]
                                # n += msg_len
                                request = hal_pb2.Request()
                                request.ParseFromString(request_raw)
                                print("Request:")
                                pprint(request)
                                response = process_request(request)
                                print("Response:")
                                pprint(response)
                                # size = response.ByteSize()
                                # conn.send(_VarintBytes(size))
                                conn.sendall(response.SerializeToString())
                            print("End of packet")
                        finally:
                            conn.close()
                            conn = None
                            break

                # keyboard interrupt must be passed to able to finish listening
                except KeyboardInterrupt:
                    raise KeyboardInterrupt

                except:
                    print("Error during establishing connection")
                    pass

                finally:
                    if conn is not None:
                        conn.close()

        except KeyboardInterrupt:
            print("Finishing listening on port ", PORT)
            pass
        finally:
            sck.close()

    run_display_task = False
    display.clear()
    pwr_selector.select_battery_source()
    if collector_positioner is not None:
        collector_positioner.finish()
    pass


if __name__ == '__main__':
    main()
