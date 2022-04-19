using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerCamaraFollow : MonoBehaviour
{
    public Transform player;
    Public Vector3 offset;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        transform.position = player.position + offset;
    }
}
