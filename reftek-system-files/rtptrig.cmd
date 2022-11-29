# Event handler command file for rtptrig for Linux

# Note: multiple instances of the command file may be running concurrently!

# This script is passed the following arguments:
#    %1 - ArcFetch criteria specification.
#    %2 - Start time as specified for Acrfetch
#    %3 - Data Stream number (N).
#    %4 - Trigger time (YYYY_MM_DD_HH_MM_SS_SSS).


# Create a unique working directory...
# --------------------------------------
mkdir /home/reftek/rtptrig/%4_%3
cd    /home/reftek/rtptrig/%4_%3

# Fetch the data from the archive...
# -------------------------------------------------------------------
/home/reftek/bin/arcfetch -c -s -o/home/reftek/rtptrig/%4_%3 /home/reftek/archive %1


