from mpi4py import MPI
comm = MPI.COMM_WORLD   # Defines the default communicator
n = comm.Get_size()  # Stores the number of processes in num_procs.
rank = comm.Get_rank()  # Stores the rank (pid) of the current process
#print("Hello world, say process ! ",rank)
data=[0]*n 
if rank==0:
   for i in range(1,n):
      comm.send(i,dest=i, tag=i)   
   for i in range(1,n):
      data[i]=comm.recv(source=MPI.ANY_SOURCE, tag=i)
   print("Root recived: ",data)
for i in range(1,n):
   if rank==i:
      a=comm.recv(source=0, tag=i)
      a=a*a
      comm.send(a,dest=0, tag=i)