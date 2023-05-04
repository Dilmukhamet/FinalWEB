
import { Component, OnInit } from '@angular/core';
import { ApiService } from './api.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{
  title = 'frontend';
  logged: boolean = false;
  mail: string = "";
  password: string = "";
  constructor(private api: ApiService){}

  ngOnInit(): void {
    console = console 
  const token = localStorage.getItem("jwt_token");
  if (token){
    this.logged =true;
  }
  }

  auth(){
    this.api.login(this.mail, this.password)
    console.log("Login from appcomponent")
    this.logged = true
  }
  exit(){
    this.api.logout()
    this.logged = false
  }
}
