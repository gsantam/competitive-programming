    chr() {
        yey=$1
        echo $yey
        printf \\$(printf '%03o' $1)
    }
    
    function hex() {
        printf '%02X\n' $1
    }
    
    function encrypt() {
        key=$1
        msg=$2
        crpt_msg=""
        # iterate over character of msg
        for ((i=0; i<${#msg}; i++)); do
            #ech character of the message
            c=${msg:$i:1}
            # ord representation of the char
            asc_chr=$(echo -ne "$c" | od -An -tuC)
            #echo $asc_chr
            key_pos=$((${#key} - 1 - ${i}))
            key_char=${key:$key_pos:1}
            #echo ${asc_chr}
            #echo $key_char
            crpt_chr=$(( $asc_chr ^ ${key_char} ))
            #echo $("$asc_chr" | bc)
            echo $crpt_chr

            hx_crpt_chr=$(hex $crpt_chr)
            #echo $hx_crpt_chr
            crpt_msg=${crpt_msg}${hx_crpt_chr}
        done
        echo $crpt_msg
    }
    
   encrypt 123238343459 hola
