import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-buttons',
  templateUrl: './buttons.component.html',
  styleUrls: ['./buttons.component.scss']
})
export class ButtonsComponent implements OnInit {


  @Input()
  type: string = "";

  @Input()
  theme: "blue"|"white"|"simple" = "white";

  @Input()
  value: string = "";

  @Input()
  imageValue: string = "";


  constructor() { }

  ngOnInit(): void {
  }

  imageButton(){
    if(this.imageValue != '') {
      return true;
    }
    return false;
  }


  checkButtonStyle(){
    switch(this.theme){
      case "blue":
        return "button-blue";
        break;
      default:
        return "button-white";
        break;
    }
  }

}