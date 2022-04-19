using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Collision : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    void onCollisionEnter(Collision collisionObject)
    {
       
       if (Equals(c.GetComponent<Collider>().tag, "Wall"))
       {
         //we hit a wall... what should we do?
          //player takes damage
}
